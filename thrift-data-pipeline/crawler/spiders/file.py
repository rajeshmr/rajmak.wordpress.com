from scrapy.spiders import CrawlSpider


class FileSpider(CrawlSpider):
    name = 'file'

    def __init__(self, filename=None, *a, **kw):
        super(FileSpider, self).__init__(*a, **kw)
        if filename:
            with open(filename, 'r') as f:
                self.start_urls = f.readlines()

    def parse(self, response):
        return {"body": response.body, "url": response.url}
