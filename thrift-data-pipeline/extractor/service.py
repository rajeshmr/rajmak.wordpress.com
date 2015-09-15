from models.ttypes import Product
from models import ParserService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import pipeline_config


class ParserServiceHandler:
    def __init__(self):
        pass

    def ping(self):
        print "ping"

    def parse(self, item):
        title = "Hello World"
        price = 100.00
        return Product(title=title, price=price)


if __name__ == '__main__':
    handler = ParserServiceHandler()
    processor = ParserService.Processor(handler)
    transport = TSocket.TServerSocket(port=pipeline_config.PARSER_SERVICE_PORT)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print "starting server"
    server.serve()
    print "Parser service OK!"
