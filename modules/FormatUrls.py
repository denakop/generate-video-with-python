from collections import defaultdict


class FormatUrls:
    def __init__(self, elastic_document, database_document):
        self.elastic_document = elastic_document
        self.database_document = database_document

    @staticmethod
    def format_urls(self):
        self.elastic_document = self.format_elastic_document(self.elastic_document)
        print(self.elastic_document)

    @staticmethod
    def format_elastic_document(urls):
        formatted_urls = defaultdict(list)
        for account_id, url_buckets in urls.items():
            for url_bucket in url_buckets:
                formatted_urls[account_id].append(url_bucket['key'])
        return formatted_urls
