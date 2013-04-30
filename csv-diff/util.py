from Levenshtein import distance
from itertools import permutations

class Util(object):
	def __init__(self):
		super(Util, self).__init__()
		self.DISTAMCE_TH = 3

	def fuzzy_equals(self,str_list):
		truth = True
		for p in permutations(str_list,2):
			if distance(p[0],p[1]) >= self.DISTAMCE_TH:
				truth = False
		return truth




		