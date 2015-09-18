from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from models import ParserService
from models.ttypes import HTML
import pipeline_config


class ThriftClientPipeline(object):
    client = None

    def __init__(self):
        try:
            socket = TSocket.TSocket(pipeline_config.PARSER_SERVICE_HOST, pipeline_config.PARSER_SERVICE_PORT)
            transport = TTransport.TBufferedTransport(socket)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            self.client = ParserService.Client(protocol)
            transport.open()
            self.client.ping()
        except Thrift.TException, tx:
            print "%s" % tx.message
            exit("Parser service not running!")

    def process_item(self, item, spider):
        html = HTML(url=item['url'], html=item['html'])
        self.client.parse(html)
        return html.url
