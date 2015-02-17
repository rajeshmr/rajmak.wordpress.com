__author__ = 'raj'

import sys
import random

import numpy

from models.vector import Vector
from models.cluster import Cluster


class KMeans:
    def __init__(self, k, max_iterations):
        self.k = k
        self.iterations = 0
        self.max_iterations = max_iterations
        self.vectors = list()
        self.initial_vectors = list()
        self.clusters = list()

    def progress(self):
        self.iterations += 1
        print self.iterations

    def add_vector(self, vid, vector_array):
        self.vectors.append(Vector(vid, vector_array))

    def initialize(self):
        self.initial_vectors = random.sample(self.vectors, self.k)
        self.clusters = [Cluster(vector) for vector in self.initial_vectors]

    def assign_vector_to_cluster(self, vector, belongs_to):
        self.clusters[belongs_to].add_vector_to_cluster(vector)
        for cid, cluster in enumerate(self.clusters):
            if cid is belongs_to:
                continue
            try:
                cluster.remove(vector)
            except KeyError:
                continue

    def run(self):
        while self.iterations <= self.max_iterations:
            self.progress()
            for vector in self.vectors:
                smallest_distance = 0
                belongs_to = 0
                for cid, cluster in enumerate(self.clusters):
                    distance = vector.get_distance_from_centroid(cluster.centroid)
                    if cid == 0 or distance < smallest_distance:
                        smallest_distance = distance
                        belongs_to = cid
                self.assign_vector_to_cluster(vector, belongs_to)
        return self.clusters


if __name__ == "__main__":
    k = int(sys.argv[1])
    iterations = int(sys.argv[2])
    kmeans = KMeans(k, iterations)

    for _vid, _vector_array in enumerate(sys.stdin):
        _vector_array = numpy.array(eval(_vector_array))
        kmeans.add_vector(_vid, _vector_array)
    kmeans.initialize()

    for _cluster in kmeans.run():
        print _cluster
        print
