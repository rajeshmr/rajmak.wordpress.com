# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider


class GenericSpider(SitemapSpider):
    name = "generic"
    sitemap_locations = ['robots.txt', 'sitemap.xml']

    def gen_sitemap_urls(self, domain):
        return map(lambda part: "%s/%s" % (domain, part), self.sitemap_locations)

    def __init__(self, domain=None, *a, **kw):
        super(GenericSpider, self).__init__(*a, **kw)
        if not domain.startswith("http"):
            domain = "http://%s" % domain
        self.name = domain
        self.sitemap_urls = self.gen_sitemap_urls(domain)

    def parse(self, response):
        return {"body": response.body, "url": response.url}
