import random
from models.vector import Vector
from models.cluster import Cluster


class KMeans:
    # k : int
    #   number of clusters required
    # iterations : int
    #       book keeping variable to keep track of number of iterations
    # max_iterations:int
    #       maximum number of iterations possible
    # vectors : list
    #       list of vecotrs
    # initial_vecotors : list[numpy_array]
    #       list of numpy_array, initial k vectors
    # clusters : list
    #       list of Cluster object

    def __init__(self, k, max_iterations):
        self.k = k
        self.iterations = 0
        self.max_iterations = max_iterations
        self.vectors = list()
        self.initial_vectors = list()
        self.clusters = list()

    # increments iteration
    def progress(self):
        self.iterations += 1

    # converts array from mapper to Vector object and adds it to KMeans class
    # vid : int,
    #       vector id
    # vector_array : numpy_array
    #       array of double of a title, from mapper.

    def add_vector(self, vid, vector_array):
        self.vectors.append(Vector(vid, vector_array))

    # K points are required to initialize the clustering process
    # K vectors are randomly selected from the list of vectors
    # and Cluster objects are constructed

    def initialize(self):
        self.initial_vectors = []
        if len(self.vectors) < self.k:
            self.initial_vectors = random.sample(self.vectors, len(self.vectors) / 2)
        else:
            self.initial_vectors = random.sample(self.vectors, self.k)
        self.clusters = [Cluster(vector) for vector in self.initial_vectors]

    # given cluster index, adds a vector to that cluster and removes the
    # same from other clusters
    # vector : numpy_array
    #       array repr of a title, from mapper.
    # belongs_to : int
    #       cluster id that vector belongs to

    def assign_vector_to_cluster(self, vector, belongs_to):
        self.clusters[belongs_to].add_vector_to_cluster(vector)
        for cid, cluster in enumerate(self.clusters):
            if cid is belongs_to:
                continue
            cluster.remove(vector)

    # for every vector,
    #   find the cluster that has smallest distance between vector and its centroid
    #   assign vector to that cluster
    #       update clusters centroid
    #       remove vector from other clusters

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
        yield self.clusters
