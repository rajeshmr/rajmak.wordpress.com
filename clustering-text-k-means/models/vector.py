__author__ = 'raj'

import sys
import numpy


class Vector:
    def __init__(self, _vid, _vector):
        self.vid = _vid
        self.co_ords = _vector
        self.distance_from_centroid = sys.maxint

    def set_distance_from_centroid(self, centroid):
        self.distance_from_centroid = numpy.linalg.norm(self.co_ords - centroid)

    def get_distance_from_centroid(self, centroid):
        return numpy.linalg.norm(self.co_ords - centroid)

    def __hash__(self):
        return self.vid

    def __eq__(self, other):
        return self.vid == other.vid

