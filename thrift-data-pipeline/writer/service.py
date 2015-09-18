from models import WriterService
import pipeline_config
from utils import thrift_utils
from writer.handler import WriterServiceHandler

if __name__ == '__main__':
    handler = WriterServiceHandler()
    server = thrift_utils.get_server(WriterService, handler, pipeline_config.WRITER_SERVICE_PORT)
    print "Starting writer server"
    server.serve()
    print "Terminating writer server"
