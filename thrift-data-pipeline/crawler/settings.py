BOT_NAME = 'sloth_crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
USER_AGENT = 'sloth_crawler (+http://rajmak.wordpress.com/)'

ITEM_PIPELINES = {
    'crawler.pipeline.ThriftClientPipeline': 10
}
