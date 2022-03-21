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

    def getImages(self, page):
        self.page = page
        htmldata = self.getdata()
        soup = BeautifulSoup(htmldata, "lxml")
        title = soup.find("meta", property="og:title")['content']
        image = soup.find("meta", property="og:image")['content']
        self.writeTextInImage(requests.get(image).content, title)

    def randomTitle(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(30))

    def writeTextInImage(self, image, title):
        self.titleCount += 1
        imageTitle = str(self.titleCount)


        file = open('assets/temporary/' + imageTitle + ".png", "wb")
        file.write(image)
        file.close()
        img = Image.open("assets/temporary/" + imageTitle + ".png")

        if (self.count == 0):
            w, h = img.size
            self.w = w
            self.h = h
            self.count += 1

        img = img.resize((self.w, self.h), Image.ANTIALIAS)
        titleFont = ImageFont.truetype('assets/fonts/PlayfairDisplay-VariableFont_wght.ttf', 12)
        editableImage = ImageDraw.Draw(img)
        text_w, text_h = editableImage.textsize(title, titleFont)
        w, h = img.size
        editableImage.text(((w - text_w) // 2, (h - text_h) - 50), title, (255, 255, 255), font=titleFont,
                           stroke_width=2, stroke_fill='black')
        img.save("assets/images/" + imageTitle + ".png")
        os.remove("assets/temporary/" + imageTitle + ".png")

    def getdata(self):
        my_session = requests.session()
        for_cookies = my_session.get(self.page)
        cookies = for_cookies.cookies
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}

        response = my_session.get(self.page, headers=headers, cookies=cookies)
        return response.text
