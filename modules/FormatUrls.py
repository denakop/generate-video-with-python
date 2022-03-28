from collections import defaultdict
from urllib.parse import urlparse
from helpers import Helpers


class FormatUrls:
    def __init__(self, elastic_document, database_document):
        self.elastic_document = elastic_document
        self.database_document = database_document
        self.helpers = Helpers

    def format_urls(self):
        self.elastic_document = self.format_elastic_document(self.elastic_document)
        return self.equals_urls(self.elastic_document, self.database_document)

    # function to get only equal urls
    @staticmethod
    def equals_urls(elastic_document, database_document):
        equal_urls = defaultdict(list)
        for key, urls in elastic_document.items():
            url = urlparse(urls[0]).netloc
            url = Helpers.remove_www(url)
            url = 'http://' + url
            if int(key) in database_document:
                if url in database_document[int(key)]:
                    equal_urls[url].append(urls)

        return equal_urls


    @staticmethod
    def format_elastic_document(urls):
        formatted_urls = defaultdict(list)
        for account_id, url_buckets in urls.items():
            for url_bucket in url_buckets:
                formatted_urls[account_id].append(url_bucket['key'])
        return formatted_urls
