from models import ParserService
import pipeline_config
from extractor.handler import ParserServiceHandler
from utils import thrift_utils

if __name__ == '__main__':
    parser_handler = ParserServiceHandler()
    server = thrift_utils.get_server(ParserService, parser_handler, pipeline_config.PARSER_SERVICE_PORT)
    print "Starting parser server"
    server.serve()
    print "Terminating parser server"
