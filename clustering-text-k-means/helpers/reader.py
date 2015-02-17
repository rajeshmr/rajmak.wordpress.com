__author__ = 'raj'
import sys


titles = open(sys.argv[1]).readlines()

for line in sys.stdin:
    splits = line.strip().split("\t")
    if line.strip() == "":
        print
    if len(splits) == 3:
        print titles[int(splits[1])].strip()

