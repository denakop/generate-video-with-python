from modules.Request import Request
from modules.GenerateVideo import GenerateVideo
from services.ElasticSearch import ElasticSearch
from services.MariaDb import MariaDb
from modules.FormatUrls import FormatUrls
from urllib.parse import urlparse

import time

start_time = time.time()


def init():
    # init and get hostnames with slider in console database
    mariadb = MariaDb()
    database_host_names = mariadb.get_host_names()

    # init and get urls from elasticsearch
    elasticsearch = ElasticSearch()
    # document = elasticsearch.get_document() # get document from elasticsearch
    document = elasticsearch.get_urls()  # test to get urls from elasticsearch without request

    # format urls to get hostnames equal to database hostnames
    format_urls = FormatUrls(document, database_host_names)
    urls = format_urls.format_urls()
    try:
        mount_video(urls)
    except Exception as e:
        print(e)


def mount_video(urls):
    request = Request()
    video_name = None
    for hostname in urls:
        request_time = time.time()
        for url in urls[hostname]:
            for href in url:
                print(href)
                request.get_images(href)
                video_name = urlparse(href).netloc
        print("Request Time %s seconds ---" % (time.time() - request_time))
        GenerateVideo(video_name)


init()
print("Total Time %s seconds ---" % (time.time() - start_time))
