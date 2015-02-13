__author__ = 'raj'

import sys
from utils import *

class Vector:
    def __init__(self, _vid, _vector):
        self.vid = _vid
        self.co_ords = _vector
        self.distance_from_centroid = sys.maxint

    def set_distance_from_centroid(self, centroid):
        self.distance_from_centroid = euclidean_distance(self.co_ords, centroid)

    def __hash__(self):
        return self.vid
