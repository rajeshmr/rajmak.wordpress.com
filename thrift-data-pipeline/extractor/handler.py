from models.ttypes import Product
from scrapy.selector import Selector
from urlparse import urlparse
from utils import thrift_utils
import pipeline_config
from models import WriterService
from thrift import Thrift


class ParserServiceHandler:
    def __init__(self):
        self.parser_meta = {
            "amazon.in": {
                "title": "//div[@id='titleSection']/h1[@id='title']/span[@id='productTitle']/text()",
                "price": "//div[@id='price']/table[@class='a-lineitem']/tbody/tr/td/span[@id='priceblock_saleprice']/text()"
            },
            "flipkart.com": {
                "title": "//div[@class='title-wrap line fk-font-family-museo section omniture-field']/h1/text()",
                "price": "//div[@class='prices']/div/span[@class='selling-price omniture-field']/text()"
            }
        }
        try:
            self.writer_client = thrift_utils.get_thrift_client(pipeline_config.WRITER_SERVICE_HOST,
                                                                pipeline_config.WRITER_SERVICE_PORT,
                                                                WriterService)
        except Thrift.TException, tx:
            print "%s" % tx.message
            exit("Writer service not running!")

    def ping(self):
        print "ping"

    def parse(self, html):
        data = dict()
        selector = Selector(text=html.html)
        domain = urlparse(html.url).netloc
        for key, xpath in self.parser_meta[domain]:
            data[key] = selector.xpath(xpath)
        product = thrift_utils.get_model(data, Product)
        self.writer_client.write(product)
