__author__ = 'raj'

import numpy


def euclidean_distance(vector_a, vector_b):
    a = numpy.array(vector_a)
    b = numpy.array(vector_b)
    return numpy.linalg.norm(a-b)