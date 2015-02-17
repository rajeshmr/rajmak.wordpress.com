__author__ = 'raj'

import sys
import re


words = set()
# bag_of_words.txt contains list of unique words
# present in the input file
for word in open("resources/bag_of_words.txt").readlines():
    words.add(word.strip())

for title in sys.stdin:
    vector = []
    title = re.sub(r"[^a-zA-Z]", " ", title).lower()
    words_in_title = map(lambda x: x.strip(), title.split())
    words_in_title = filter(lambda x: len(x) > 2, words_in_title)
    # for every word count the frequency of the word,
    # which represents a point in the vector
    for word in words:
        count = len(filter(lambda x: x in word, words_in_title))
        vector.append(float(count))
    print vector