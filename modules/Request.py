import random
import string
import requests
import os

from bs4 import BeautifulSoup
from PIL import ImageFont, ImageDraw, Image


class Request:
    def __init__(self):
        self.w = 0
        self.h = 0
        self.count = 0
        self.page = ''
        self.titleCount = 0

    def get_images(self, page):
        self.page = page
        htmldata = self.get_data()
        soup = BeautifulSoup(htmldata, "lxml")
        title = soup.find("meta", property="og:title")['content']
        image = soup.find("meta", property="og:image")['content']
        self.write_text_in_image(requests.get(image).content, title)

    @staticmethod
    def random_title():
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(30))

    def write_text_in_image(self, image, title):
        self.titleCount += 1
        image_title = str(self.titleCount)

        with open('assets/temporary/' + image_title + ".jpg", 'wb') as handler:
            handler.write(image)

        img = Image.open("assets/temporary/" + image_title + ".jpg")

        if self.count == 0:
            w, h = img.size
            self.w = w
            self.h = h
            self.count += 1

        img = img.resize((self.w, self.h), Image.ANTIALIAS)
        title_font = ImageFont.truetype('assets/fonts/PlayfairDisplay-VariableFont_wght.ttf', 12)
        editable_image = ImageDraw.Draw(img)
        text_w, text_h = editable_image.textsize(title, title_font)
        w, h = img.size
        editable_image.text(((w - text_w) // 2, (h - text_h) - 50), title, (255, 255, 255), font=title_font,
                            stroke_width=2, stroke_fill='black')
        img.save("assets/images/" + image_title + ".jpg")
        os.remove("assets/temporary/" + image_title + ".jpg")

    def get_data(self):
        my_session = requests.session()
        for_cookies = my_session.get(self.page)
        cookies = for_cookies.cookies
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}

        response = my_session.get(self.page, headers=headers, cookies=cookies)
        return response.text
