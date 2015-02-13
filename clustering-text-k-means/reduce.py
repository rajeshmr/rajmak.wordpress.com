__author__ = 'raj'

import sys
import random
from vector import Vector
from cluster import Cluster
from utils import euclidean_distance


class KMeans:
    def __init__(self, k):
        self.k = k
        self.iterations = 0
        self.max_iterations = 1000
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
                    distance = euclidean_distance(vector.co_ords, cluster.centroid)
                    if cid == 0 or distance < smallest_distance:
                        smallest_distance = distance
                        belongs_to = cid
                self.assign_vector_to_cluster(vector, belongs_to)
        return self.clusters


if __name__ == "__main__":
    titles = open("sample_input.txt").readlines()
    kmeans = KMeans(20)

    for _vid, _vector_array in enumerate(sys.stdin):
        kmeans.add_vector(_vid, eval(_vector_array))
    kmeans.initialize()

    for _cluster in kmeans.run():
        for v in _cluster.vectors:
            print v.distance_from_centroid, titles[v.vid].strip()
        print "-" * 10