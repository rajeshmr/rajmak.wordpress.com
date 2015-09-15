BOT_NAME = 'rajmak-bot'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
USER_AGENT = 'rajmak-bot (+http://rajmak.wordpress.com/)'

ITEM_PIPELINES = {
    'crawler.pipeline.ThriftClientPipeline': 10
}
DOWNLOAD_DELAY = 1
