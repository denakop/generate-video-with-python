from modules.Request import Request
from modules.GenerateVideo import GenerateVideo
from helpers import Helpers
from services.ElasticSearch import ElasticSearch
from services.MariaDb import MariaDb
from modules.FormatUrls import FormatUrls
from urllib.parse import urlparse
import concurrent.futures

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
    for hostname in urls:
        request_time = time.time()
        for url in urls[hostname]:
            multi_requests(url)
        print("Request Time %s seconds ---" % (time.time() - request_time))
        GenerateVideo(Helpers.remove_www(urlparse(hostname).netloc))


def multi_requests(urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for url in urls:
            futures.append(executor.submit(request.get_images, page=url))


request = Request()
init()
print("Total Time %s seconds ---" % (time.time() - start_time))

