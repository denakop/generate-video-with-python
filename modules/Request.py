import random
import string
import requests
import os
import json

from urllib.parse import urlparse
from bs4 import BeautifulSoup
from PIL import ImageFont, ImageDraw, Image, ImageFile
from helpers import Helpers


class Request:
    def __init__(self):
        self.w = 0
        self.h = 0
        self.count = 0
        self.titleCount = 0

    def get_images(self, page):
        htmldata = self.get_data(page)
        soup = BeautifulSoup(htmldata, "lxml")
        title = soup.find("meta", property="og:title")['content']
        image = None

        if image is None:
            try:
                image = soup.find("meta", property="og:image")['content']
            except:
                image = 'none'  # todo add default image
        self.write_text_in_image(requests.get(image).content, title, page)

    # slow method
    @staticmethod
    def get_url_image(soup):
        yoast = json.loads("".join(soup.find("script", {"type": "application/ld+json"}).contents))

        if '@graph' in yoast:
            for item in yoast['@graph']:
                if item['@type'] == 'ImageObject':
                    return item['url']
        elif 'image' in yoast:
            return yoast['image']['url']

        return None

    @staticmethod
    def random_title():
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(30))

    def write_text_in_image(self, image, title, page):
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        self.titleCount += 1
        image_title = str(self.titleCount)

        with open('assets/temporary/' + image_title + ".jpeg", 'wb') as handler:
            handler.write(image)

        try:
            img = Image.open("assets/temporary/" + image_title + ".jpeg").convert('RGB')
        except:
            img = Image.open("assets/no-image.jpg").convert('RGB')

        if self.count == 0:
            w, h = img.size
            self.w = w
            self.h = h
            self.count += 1

        img = img.resize((self.w, self.h), Image.ANTIALIAS)
        editable_image = ImageDraw.Draw(img, 'RGBA')
        w, h = img.size
        font_size = self.get_font_size(title, 'assets/fonts/times.ttf', w, h, editable_image) - 1
        title_font = ImageFont.truetype('assets/fonts/times.ttf', font_size)

        text_w, text_h = editable_image.textsize(title, title_font)
        shape = ((5, h - 100), (w - 5, h - 10))
        editable_image.rectangle(shape, fill=(0, 0, 0, 180))
        editable_image.text(((w - text_w) // 2, (h - text_h) - 50), title, font=title_font, fill=(255, 255, 255))
        dir = urlparse(page).netloc
        dir = Helpers.remove_www(dir)

        if os.path.isdir('assets/images/' + dir) is False:
            os.mkdir('assets/images/' + dir)
        img.save("assets/images/" + dir + "/" + image_title + ".jpeg")

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

    def get_data(self, page):
        my_session = requests.session()
        for_cookies = my_session.get(page)
        cookies = for_cookies.cookies
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}

        response = my_session.get(page, headers=headers, cookies=cookies)
        return response.text
