import os

from modules.Request import Request
from modules.GenerateVideo import GenerateVideo
from helpers import Helpers
from services.ElasticSearch import ElasticSearch
from services.MariaDb import MariaDb
from modules.FormatUrls import FormatUrls
from urllib.parse import urlparse
from os import path

import concurrent.futures
import time

start_time = time.time()


def init():
    # init and get hostnames with slider in console database
    mariadb = MariaDb()
    database_host_names = mariadb.get_host_names()

    # init and get urls from elasticsearch
    elasticsearch = ElasticSearch()
    document = elasticsearch.get_document() # get document from elasticsearch
    # document = elasticsearch.get_urls()  # test to get urls from elasticsearch without request

    # format urls to get hostnames equal to database hostnames
    format_urls = FormatUrls(document, database_host_names)
    urls = format_urls.format_urls()
    # try:
    print("Começando requests")
    mount_video(urls)
    # except Exception as e:
    #     print(e)


def mount_video(urls):
    account_id = None
    for hostname in urls:
        count = 0
        request_time = time.time()
        for url in urls[hostname]:
            if count == 0:
                account_id = url['account_id']
                count += 1
            else:
                multi_requests(url)
        url_host_name = Helpers.remove_www(urlparse(hostname).netloc)
        path_images = "assets/images/" + url_host_name
        if path.exists(path_images):
            if os.listdir():
                GenerateVideo(url_host_name, account_id)
                print("Request Time %s seconds ---" % (time.time() - request_time))


def multi_requests(urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for url in urls:
            futures.append(executor.submit(request.get_images, page=url))


request = Request()
init()
print("Total Time %s seconds ---" % (time.time() - start_time))

