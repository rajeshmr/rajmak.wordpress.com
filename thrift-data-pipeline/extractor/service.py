import logging
from logging.config import fileConfig
import sys

from models import ParserService
import pipeline_config
from extractor.handler import ParserServiceHandler
from utils import thrift_utils

if __name__ == '__main__':
    fileConfig()
    parser_handler = ParserServiceHandler()
    server = thrift_utils.get_server(ParserService, parser_handler, pipeline_config.PARSER_SERVICE_PORT)
    logging.info("Starting parser server")
    try:
        server.serve()
    except KeyboardInterrupt:
        logging.info("Terminating parser server")
