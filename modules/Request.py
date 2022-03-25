import random
import string
import requests
import os

from bs4 import BeautifulSoup
from PIL import ImageFont, ImageDraw, Image, ImageFile


class Request:
    def __init__(self):
        self.w = 0
        self.h = 0
        self.count = 0
        self.page = ''
        self.titleCount = 0
        self.default_url = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'

    def get_images(self, page):
        self.page = page
        htmldata = self.get_data()
        soup = BeautifulSoup(htmldata, "lxml")
        title = soup.find("meta", property="og:title")['content']
        try:
            image = soup.find("meta", property="og:image")['content']
        except:
            image = self.default_url  # todo add default image
        self.write_text_in_image(requests.get(image).content, title)

    @staticmethod
    def random_title():
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(30))

    def write_text_in_image(self, image, title):
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        self.titleCount += 1
        image_title = str(self.titleCount)

        with open('assets/temporary/' + image_title + ".jpeg", 'wb') as handler:
            handler.write(image)

        try:
            img = Image.open("assets/temporary/" + image_title + ".jpeg").convert('RGB')
        except:
            img = Image.open(requests.get(self.default_url, stream=True).raw).convert('RGB')

        if self.count == 0:
            w, h = img.size
            self.w = w
            self.h = h
            self.count += 1

        img = img.resize((self.w, self.h), Image.ANTIALIAS)
        editable_image = ImageDraw.Draw(img, 'RGBA')
        w, h = img.size
        font_size = self.get_font_size(title, 'assets/fonts/PlayfairDisplay-VariableFont_wght.ttf', w, h, editable_image) - 1
        title_font = ImageFont.truetype('assets/fonts/PlayfairDisplay-VariableFont_wght.ttf', font_size)

        text_w, text_h = editable_image.textsize(title, title_font)
        print(text_w, text_h)
        print(w, h)
        shape = ((5, h - 100), (w - 5, h - 10))
        editable_image.rectangle(shape, fill=(0, 0, 0, 180))
        editable_image.text(((w - text_w) // 2, (h - text_h) - 50), title, font=title_font, fill=(255, 255, 255))
        img.save("assets/images/" + image_title + ".jpeg")
        os.remove("assets/temporary/" + image_title + ".jpeg")

    @staticmethod
    def get_font_size(text, font_name, width, height, img_draw):
        # default values at start
        font_size = None  # for font size

        # test for different font sizes
        for size in range(1, 500):

            # create new font
            new_font = ImageFont.truetype(font_name, size)

            # calculate bbox for version 8.0.0
            new_box = img_draw.textbbox((0, 0), text, new_font)  # need 8.0.0

            # `bbox` may have top/left margin so calculate real width/height
            new_w = new_box[2] - new_box[0]  # bottom-top
            new_h = new_box[3] - new_box[1]  # right-left
            # print(size, '|', new_w, new_h, '|', new_box)

            # if too big then exit with previous values
            if new_w > width or new_h > height:
                break

            # set new current values as current values
            font_size = size
            font = new_font
            box = new_box
            w = new_w
            h = new_h

            # calculate position (minus margins in box)
            x = (width - w) // 2 - box[0]  # minus left margin
            y = (height - h) // 2 - box[1]  # minus top margin

        return font_size

    def get_data(self):
        my_session = requests.session()
        for_cookies = my_session.get(self.page)
        cookies = for_cookies.cookies
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}

        response = my_session.get(self.page, headers=headers, cookies=cookies)
        return response.text
