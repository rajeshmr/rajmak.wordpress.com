import logging
import sys

from models import WriterService
import pipeline_config
from utils import thrift_utils
from writer.handler import WriterServiceHandler

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    handler = WriterServiceHandler()
    server = thrift_utils.get_server(WriterService, handler, pipeline_config.WRITER_SERVICE_PORT)
    logging.info("Starting writer server")
    server.serve()
    logging.info("Terminating writer server")
