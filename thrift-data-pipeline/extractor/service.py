from models import ParserService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import pipeline_config
from handler import ParserServiceHandler

if __name__ == '__main__':
    handler = ParserServiceHandler()
    processor = ParserService.Processor(handler)
    transport = TSocket.TServerSocket(port=pipeline_config.PARSER_SERVICE_PORT)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print "Starting parser server"
    server.serve()
    print "Terminating parser server"
