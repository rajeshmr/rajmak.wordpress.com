__author__ = 'raj'

import sys
import numpy


class Vector:

    # Vector representation of a title
    # vid - int, Vector ID.
    # co_ords - numpy_array representation of a title.
    # distance_from_centroid - euclidean distance from the centroid of the cluster it belongs to
    def __init__(self, _vid, _vector):
        self.vid = _vid
        self.co_ords = _vector
        self.distance_from_centroid = sys.maxint

    # euclidean distance from this and the given centroid
    # getter
    def set_distance_from_centroid(self, centroid):
        self.distance_from_centroid = numpy.linalg.norm(self.co_ords - centroid)

    # setter
    def get_distance_from_centroid(self, centroid):
        return numpy.linalg.norm(self.co_ords - centroid)

    def __hash__(self):
        return self.vid

    def __eq__(self, other):
        return self.vid == other.vid

