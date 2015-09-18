from models.ttypes import Product
from scrapy.selector import Selector
from urlparse import urlparse


class ParserServiceHandler:
    def __init__(self):
        self.parser_meta = {
            "amazon.in":{
                "title": "//div[@id='titleSection']/h1[@id='title']/span[@id='productTitle']",
                "price": "//div[@id='price']/table[@class='a-lineitem']/tbody/tr/td/span[@id='priceblock_saleprice']"
            },
            "flipkart.com":{
                "title": "//div[@class='title-wrap line fk-font-family-museo section omniture-field']/h1[@class='title']",
                "price": ""
            }
        }

    def ping(self):
        print "ping"

    def parse(self, html):
        selector = Selector(text=html.html)
        parsed_url = urlparse(html.url)
        # for key, selector in self.parser_meta[parsed_url.netloc]:

        title = "Hello World"
        price = 100.00
        return Product(title=title, price=price)
