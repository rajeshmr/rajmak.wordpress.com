__author__ = 'raj'
import sys
import re

bag_of_words = set()
for title in sys.stdin:
    title = re.sub(r"[^a-zA-Z]", " ", title).lower()
    for word in filter(lambda x: len(x) > 2, title.split()):
        bag_of_words.add(word.strip())

for word in bag_of_words:
    print word


