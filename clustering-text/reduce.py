import sys
from Levenshtein import distance
import json

DISTANCE = 25
cluster = {}
cid = 0

for i, line in enumerate(sys.stdin):
    cols = line.strip().split("\t")
    if i == 0:
        cluster[cid] = []
        cluster[cid].append(cols)
    else:
        last = cluster[cid][-1]
        if distance(last[0], cols[0]) <= DISTANCE:
            cluster[cid].append(cols)
        else:
            cid += 1
            cluster[cid] = []
            cluster[cid].append(cols)

for k, v in cluster.iteritems():
    print
    print "Cluster # ", k
    for entry in v:
        print entry[1]
