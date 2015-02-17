__author__ = 'raj'

import sys
import re


words = list()
for word in open("resources/bag_of_words.txt").readlines():
    words.append(word.strip())

for title in sys.stdin:
    vector = []
    title = re.sub(r"[^a-zA-Z]", " ", title).lower()
    words_in_title = map(lambda x: x.strip(), title.split())
    words_in_title = filter(lambda x: len(x) > 2, words_in_title)

    for word in words:
        count = len(filter(lambda x: x in word, words_in_title))
        vector.append(float(count))
    print vector