__author__ = 'raj'

import csv

import MySQLdb as mdb
import re


class PreProcessing:
    def __init__(self):
        self.db = mdb.connect("localhost", "root", "123456", "lsh")
        self.cursor = self.db.cursor()
        self.stopwords = [word.strip() for word in open("stopwords.txt").readlines()]
        self.hash = json.loads("hash.json")
        self.D = self.get_dictionary_size()

    def get_dictionary_size(self):
        return 1

    def hash(self, row, index):
        return (((self.hash[index][0] * row) + self.hash[index][1]) % 257885161) % self.D

    def get_shingles(self, string, size=3):
        token_list = string.lower().strip().split()
        token_list = map(lambda x: re.sub(r"[^a-zA-Z0-9]", " ", x).strip(), token_list)
        token_list = filter(lambda x: x is not "" and x not in self.stopwords, token_list)
        for i in range(0, len(token_list) - size + 1):
            yield token_list[i:i + size]

    def insert_shingle(self, word_list):
        sql = "INSERT INTO `lsh`.`lsh_shingles` (`id`, `keyword`) VALUES (NULL, '%s');" % " ".join(word_list)
        self.cursor.execute(sql)
        return self.cursor.lastrowid

    def get_shingle_id(self, word_list):
        sid = -1
        sql = """ SELECT * FROM `lsh_shingles` WHERE `keyword` LIKE "%s"  """ % " ".join(word_list)
        try:
            self.cursor.execute(sql)
            sid = self.cursor.fetchone()[0]
        except:
            sid = self.insert_shingle(word_list)
        return sid

    def shingle_and_hash(self, doc):
        shingles = self.get_shingles(doc)
        for shingle in shingles:
            sid = self.get_shingle_id(shingle)






    def end(self):
        self.db.commit()
        self.db.close()


if __name__ == "__main__":
    pp = PreProcessing()
    with open('/home/raj/Downloads/news_newsfeed.csv', 'rb') as csvfile:
        f = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in f:
            doc = "%s %s" % (row[1], row[2])
            pp.shingle_and_hash(doc)
    pp.end()