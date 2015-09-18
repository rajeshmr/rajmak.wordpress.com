import sqlite3
import pipeline_config
import json


class WriterServiceHandler:
    insert_query = "insert into product(title, price, in_stock) values ('{title}', '{price}', '{in_stock}')"

    def __init__(self):
        self.conn = sqlite3.connect(pipeline_config.DB_LOCATION)
        self.json_file = open(pipeline_config.JSON_DUMP, 'w')

    def __del__(self):
        self.conn.close()
        self.json_file.close()

    def ping(self):
        print "ping"

    def sqlite_writer(self, product):
        sql = self.insert_query.format(title=product.title, price=product.price, in_stock=product.in_stock)
        self.conn.execute(sql)

    def json_line_writer(self, product):
        d = {"title": product.title, "price": product.price, "in_stock": product.in_stock}
        dump = json.dumps(d)
        self.json_file.write(dump)

    def write(self, product):
        self.sqlite_writer(product)
