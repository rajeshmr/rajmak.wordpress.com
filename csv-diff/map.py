import sys
import os
import csv
import json
from fingerprint import FingerPrint

inputpath = "input"
f = FingerPrint()

for txtfile in os.listdir(inputpath):
	csvfile = csv.DictReader(open(inputpath + "/" + txtfile,'rb'),)
	for record in csvfile:
		print "\t".join([f.bigram_fingerprint(record['company_name']),record['company_name'], txtfile, json.dumps(record)])