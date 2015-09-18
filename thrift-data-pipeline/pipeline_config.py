import os

PARSER_SERVICE_HOST = 'localhost'
PARSER_SERVICE_PORT = 8090

WRITER_SERVICE_HOST = 'localhost'
WRITER_SERVICE_PORT = 8091

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
DB_LOCATION = "%s/%s" % (PROJECT_DIR, "crawl.db")
DB_SCHEMA = "%s/%s" % (PROJECT_DIR, "schema.sql")
JSON_DUMP = "%s/%s" % (PROJECT_DIR, "crawl.jsonline")
