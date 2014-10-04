__author__ = 'raj'

import json
import pymysql, re


class MinHash:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', port=8889, user='root', passwd='123456', db='mysql')
        self.cursor = self.db.cursor()
        self.stopwords = [word.strip() for word in open("stopwords.txt").readlines()]

        self.hash = json.loads(open("hash.json").read())
        self.P = 257885161
        self.D = self.get_dictionary_size()

    def get_dictionary_size(self):
        sql = """SELECT COUNT(*) FROM `rajmak`.`lsh_shingles`;"""
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]

    def get_shingles(self, string, size=3):
        token_list = string.lower().strip().split()
        token_list = map(lambda x: re.sub(r"[^a-zA-Z0-9]", " ", x).strip(), token_list)
        token_list = filter(lambda x: x is not "" and x not in self.stopwords, token_list)
        for i in range(0, len(token_list) - size + 1):
            yield token_list[i:i + size]

    def get_shingle_id(self, shingle):
        sql = """ SELECT id from `rajmak`.`lsh_shingles` WHERE keyword LIKE '%s' """ % " ".join(shingle)
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]

    def shingle_and_hash(self, doc, doc_id):
        for shingle in self.get_shingles(doc):
            sid = self.get_shingle_id(shingle)
            self.apply_all_hash(doc_id, sid)

    def get_hash(self, row, A, B):
        return (((A * row) + B) % 257885161) % self.D

    def apply_all_hash(self, doc_id, sid):
        for hi, h in enumerate(self.hash):
            hx = self.get_hash(sid, h[0], h[1])
            self.insert_min_hash(doc_id, hi, hx)

    def get_doc_min_hash(self, doc_id, hid):
        sql = """ SELECT * FROM `lsh_min_hash` WHERE `doc_id` = %d AND `hash_id` = %d """ % (doc_id, hid)
        try:
            self.cursor.execute(sql)
            hx = self.cursor.fetchone()[3]
        except:
            hx = None
        return hx

    def insert_min_hash(self, doc_id, hash_id, hx):
        ex_hx = self.get_doc_min_hash(doc_id, hash_id)
        if hx < ex_hx and ex_hx is not None:
            self.replace_hash(doc_id, hash_id, hx)
        else:
            self.insert_new_hash(doc_id, hash_id, hx)

    def replace_hash(self, doc_id, hash_id, hx):
        sql = """ UPDATE `rajmak`.`lsh_min_hash` SET `min_hash` = '%d' WHERE `lsh_min_hash`.`doc_id` = %d AND `lsh_min_hash`.`hash_id` = %d;  """ % (hx, doc_id, hash_id)
        self.cursor.execute(sql)
        return self.cursor.lastrowid

    def insert_new_hash(self, doc_id, hash_id, hx):
        sql = """INSERT INTO `rajmak`.`lsh_min_hash` (`id`, `doc_id`, `hash_id`, `min_hash`) VALUES (NULL, '%d', '%d', '%d');""" % (doc_id, hash_id, hx)
        self.cursor.execute(sql)
        return self.cursor.lastrowid

    def read_feeds(self):
        sql = """ SELECT * FROM `rajmak`.`news_newsfeed` """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def end(self):
        self.db.commit()
        self.db.close()



if __name__ == "__main__":
    m = MinHash()
    for row in m.read_feeds():
        doc = "%s %s" % (row[1], row[2])
        m.shingle_and_hash(doc, row[0])
    m.end()
