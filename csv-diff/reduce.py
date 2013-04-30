import sys
from operator import itemgetter
from itertools import groupby
from util import Util
import csv



def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator)

data = read_mapper_output(sys.stdin,"\t")
u = Util()
output_file = open('output.csv','wb')
fieldnames = ['website', 'city', 'fax', 'po_box_zip', 'zip', 'toll_free', 'op_address_source', 'po_box_city', 'po_box_state', 'phone', 'state', 'op_po_box_source', 'address_1', 'address_2', 'po_box', 'company_email', 'id', 'company_name']
csvwriter = csv.DictWriter(output_file, delimiter=',',fieldnames=fieldnames)

for fp, group in groupby(data,itemgetter(0)):
	group = list(group)
	headers = [set(eval(x[3]).keys()) for x in group]
	records = [eval(x[3]) for x in group]
	if len(headers) > 1:
		common_headers = set.intersection(*headers)
		for h in common_headers:
			values = [record[h] for record in records]
		if u.fuzzy_equals(values):
			for g in group:
				csvwriter.writerow(eval(g[3]))


	
		

	# g = list(group)
	# if len(g) > 1:
	# 	for k in set(eval(g[0][3]).keys()).intersection(eval(g[1][3]).keys()):
