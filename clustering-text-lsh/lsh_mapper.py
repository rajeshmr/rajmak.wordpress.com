__author__ = 'raj'
import sys
from random import randrange

word_ids = dict()
num_hashes = 10
num_per_band = 2

a_hash = [randrange(sys.maxint) for _ in xrange(0, num_hashes)]
b_hash = [randrange(sys.maxint) for _ in xrange(0, num_hashes)]


def min_hash_fn(a, b, sig):
    hashes = [((a * x) + b) % len(word_ids) for x in sig]
    return min(hashes)


def get_min_hash_row(sig):
    hashes = [min_hash_fn(a, b, sig) for a, b in zip(a_hash, b_hash)]
    return hashes


def get_band(l, n):
    for i in xrange(0, len(l), n):
        yield frozenset(l[i:i+n])


for word, wid in map(lambda x: x.split(), open("sample_dict.txt").readlines()):
    word_ids[word] = int(wid)

for doc_id, doc in enumerate(sys.stdin):
    words = doc.strip().lower().split()

    signature = map(lambda x: word_ids.get(x), words)
    signature = filter(lambda x: x is not None, signature)

    min_hash_row = get_min_hash_row(signature)

    banded = get_band(min_hash_row, num_per_band)

    for band_id, band in enumerate(banded):
        print "%d\t%d\t%d" % (band_id, hash(band), doc_id)