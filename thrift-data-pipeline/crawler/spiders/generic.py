# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import SitemapSpider
from scrapy.selector import Selector
from crawler.models.product import ProductItem
import json
import os


class GenericSpider(SitemapSpider):

    name = "generic"
    path = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, parser_name=None, *a, **kw):
        super(GenericSpider, self).__init__(*a, **kw)
        self.name = parser_name
        self.parser_file = open("%s/../parser_meta/%s.json" % (self.path, parser_name)).read()
        self.parser_meta = json.loads(self.parser_file)
        self.allowed_domains = self.parser_meta["allowed_domains"]
        self.sitemap_urls = self.parser_meta["sitemap_urls"]

    @staticmethod
    def get_string(selector, xpath):
        return selector.xpath(xpath).extract()

    @staticmethod
    def get_list(selector, xpath, items):
        tags = selector.xpath(xpath)
        tags = map(lambda x: x.xpath(items).extract(), tags)
        tags = map(lambda x: x[0] if x is not None or x is not [] else [], tags)
        tags = filter(lambda x: x is not None or x is not [], tags)
        return tags

    def parse(self, response):
        item = ProductItem()
        sel = Selector(response)
        for key, value in self.parser_meta["selectors"].iteritems():
            if value["type"] == "string":
                item[key] = self.get_string(sel, value["selector"])
            elif value["type"] == "list":
                item[key] = self.get_list(sel, value["selector"], value["items"])
            else:
                print "invalid selector config"
        return item
