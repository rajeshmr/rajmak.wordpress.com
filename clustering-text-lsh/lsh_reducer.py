__author__ = 'raj'

import sys

prev_band_id, prev_band_hash = None, None
cluster = []
cid = 0

for line in sys.stdin:
    band_id, band_hash, doc_id = line.strip().split("\t", 3)

    if prev_band_id is None and prev_band_hash is None:
        prev_band_id, prev_band_hash = band_id, band_hash

    if prev_band_id is band_id:
        if prev_band_hash == band_hash:
            cluster.append(doc_id)
        else:
            print cid, cluster
            cluster = [doc_id]
    else:
        print cid, cluster
        cluster = [doc_id]
        cid += 1
    prev_band_id, prev_band_hash = band_id, band_hash
