__author__ = 'raj'

import re

import pymysql


class PreProcessing:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', port=8889, user='root', passwd='123456', db='mysql')
        self.cursor = self.db.cursor()
        self.stopwords = [word.strip() for word in open("stopwords.txt").readlines()]

    def get_shingles(self, string, size=3):
        token_list = string.lower().strip().split()
        token_list = map(lambda x: re.sub(r"[^a-zA-Z0-9]", " ", x).strip(), token_list)
        token_list = filter(lambda x: x is not "" and x not in self.stopwords, token_list)
        for i in range(0, len(token_list) - size + 1):
            yield token_list[i:i + size]

    def insert_shingle(self, word_list):
        sql = "INSERT INTO `rajmak`.`lsh_shingles` (`id`, `keyword`) VALUES (NULL, '%s');" % " ".join(word_list)
        try:
            self.cursor.execute(sql)
        except:
            pass

    def shingle(self, doc):
        shingles = self.get_shingles(doc)
        for shingle in shingles:
            self.insert_shingle(shingle)

    def end(self):
        self.db.commit()
        self.db.close()

    def read_feeds(self):
        sql = """ SELECT * FROM `rajmak`.`news_newsfeed` """
        self.cursor.execute(sql)
        return self.cursor.fetchall()


if __name__ == "__main__":
    pp = PreProcessing()
    for row in pp.read_feeds():
        doc = "%s %s" % (row[1], row[2])
        pp.shingle(doc)
    pp.end()