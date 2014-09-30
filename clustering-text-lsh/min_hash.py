__author__ = 'raj'

import json


class MinHash:
    def __init__(self, D):
        self.hash = json.loads("hash.json")
        self.P = 257885161
        self.D = D

    def hash(self, row, index):
        return (((self.hash[index][0] * row) + self.hash[index][1]) % self.P) % self.D

