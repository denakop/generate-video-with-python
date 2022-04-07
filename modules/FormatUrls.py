from collections import defaultdict
from datetime import datetime, timedelta
from urllib.parse import urlparse
from helpers import Helpers
from services.Jenkins import Jenkins


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
        date_less_three_days = datetime.now() - timedelta(days=3)
        date_less_three_days = date_less_three_days.date()
        equal_urls = defaultdict(list)
        # jenkins = Jenkins()
        for key, urls in elastic_document.items():
            url = urlparse(urls[0]).netloc
            url = Helpers.remove_www(url)
            url = 'http://' + url
            for item in database_document:
                if int(key) in item:
                    if item[int(key)]['url'] == url:
                        if item[int(key)]['video_date'] is None:
                            equal_urls[url].append({'account_id': key})
                            equal_urls[url].append(urls)
                            # jenkins.send_request_to_jenkins(account_id=key)
                        elif item[int(key)]['video_date'] > date_less_three_days:
                            equal_urls[url].append({'account_id': key})
                            equal_urls[url].append(urls)
        return equal_urls


    @staticmethod
    def format_elastic_document(urls):
        formatted_urls = defaultdict(list)
        for account_id, url_buckets in urls.items():
            for url_bucket in url_buckets:
                formatted_urls[account_id].append(url_bucket)
        return formatted_urls
