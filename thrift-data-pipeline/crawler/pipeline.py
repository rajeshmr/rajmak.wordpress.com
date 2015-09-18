from thrift import Thrift
from models import ParserService
from models.ttypes import HTML
import pipeline_config
from utils import thrift_utils


class ThriftClientPipeline(object):
    client = None

    def __init__(self):
        try:
            self.client = thrift_utils.get_thrift_client(pipeline_config.PARSER_SERVICE_HOST,
                                                         pipeline_config.PARSER_SERVICE_PORT,
                                                         ParserService)
        except Thrift.TException, tx:
            print "%s" % tx.message
            exit("Parser service not running!")

    def process_item(self, item, spider):
        html = HTML(url=item['url'], html=item['body'])
        self.client.parse(html)
        return html.url
