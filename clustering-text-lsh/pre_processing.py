__author__ = 'raj'

import csv

import MySQLdb as mdb
from utils import Utils


class PreProcessing:
    def __init__(self):
        self.db = mdb.connect("localhost", "root", "123456", "lsh")
        self.cursor = self.db.cursor()
        self.utils = Utils()

    def insert_shingle(self, word_list):
        sql = "INSERT INTO `lsh`.`lsh_shingles` (`id`, `keyword`) VALUES (NULL, '%s');" % " ".join(word_list)
        try:
            self.cursor.execute(sql)
        except IntegrityError:

        except KeyboardInterrupt:
            self.end()
            exit()
        except Exception as e:
            pass
        return self.cursor.lastrowid

    def generate_dictionary(self, string):
        shingles = self.utils.get_shingles(string, 3)
        return self.insert_shingle(shingles)

    def end(self):
        self.db.commit()
        self.db.close()

if __name__ == "__main__":
    pp = PreProcessing()
    with open('/home/raj/Downloads/news_newsfeed.csv', 'rb') as csvfile:
        f = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in f:
            doc = "%s %s" % (row[1], row[2])
            pp.generate_dictionary(doc)
    pp.end()