__author__ = 'raj'
import  re


class Utils:
    def __init__(self):
        self.stopwords = [word.strip() for word in open("stopwords.txt").readlines()]

    def get_shingles(self, string, size):
        token_list = string.lower().strip().split()
        token_list = map(lambda x: re.sub(r"[^a-zA-Z0-9]", " ", x).strip(), token_list)
        token_list = filter(lambda x: x is not "" and x not in self.stopwords, token_list)
        for i in range(0, len(token_list) - size + 1):
            yield token_list[i:i + size]
