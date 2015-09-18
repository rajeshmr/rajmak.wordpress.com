from __future__ import with_statement
from contextlib import contextmanager as _contextmanager
from fabric.api import *
import os


@task
def host_type():
    local('uname -s')


@_contextmanager
def virtualenv(pwd):
    with cd(pwd):
        local("virtualenv --no-site-packages .env")
        with prefix("source %s/.env/bin/activate" % pwd):
            yield


def runbg(cmd, sockname="dtach"):
    return run('dtach -n `mktemp -u /tmp/%s.XXXX` %s' % (sockname, cmd), shell="/bin/bash")


def start_parser_service():
    print "starting parser service"
    runbg("bin/python extractor/service.py")


def start_writer_service():
    print "starting writer service"
    runbg("bin/python writer/service.py")


def start_amazon_crawler():
    print "start amazon crawler"
    local("bin/scrapy crawl -a domain=amazon.in generic", shell="/bin/bash")


def start_flipkart_crawler():
    print "start flipkart crawler"
    local("bin/scrapy crawl -a domain=flipkart.com generic", shell="/bin/bash")


def kill_services():
    local("ps waux | grep service.py | awk -F" " '{print $2}'| xargs kill", shell="/bin/bash")


def init_db():
    local("bin/python init_db.py")


@task
def build(pwd=os.path.dirname(os.path.realpath(__file__))):
    with virtualenv(pwd):
        local("python bootstrap.py", shell="/bin/bash")
        local("python bin/buildout", shell="/bin/bash")
        local("python init_db.py", shell="/bin/bash")



@task
def start_pipeline(pwd=os.path.dirname(os.path.realpath(__file__))):
    with virtualenv(pwd):
        start_parser_service()
        start_writer_service()
        # start_amazon_crawler()
        # start_flipkart_crawler()
