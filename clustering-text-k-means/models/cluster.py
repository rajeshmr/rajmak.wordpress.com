__author__ = 'raj'
import numpy


class Cluster:

    # Cluster, model with helper functions to manage list of vectors
    # vector: set of Vector
    #       vectors belong to cluster
    # centroid: numpy_array
    #       average of points in a vector
    # cid: int
    #       Unique cluster identifier
    def __init__(self, _initial_vector):
        self.vectors = {_initial_vector}
        self.centroid = self.calculate_centroid()
        self.cid = self.centroid.__hash__()

    # to string
    def __repr__(self):
        out = ["%d\t%d\t%f" % (self.cid, v.vid, v.get_distance_from_centroid(self.centroid)) for v
               in self.vectors]
        return "\n".join(out)

    # remove vector from cluster
    # vector: Vector
    #       vector to be removed
    def remove(self, vector):
        if vector in self.vectors:
            self.vectors.remove(vector)
            self.calculate_centroid()

    # add vector to cluster
    # _vector: Vector
    #       add vector to cluster and update centroid
    def add_vector_to_cluster(self, _vector):
        _vector.set_distance_from_centroid(self.centroid)
        self.vectors.add(_vector)
        return ",".join(map(str, self.calculate_centroid()))

    # sum of vector
    # vectors =[ [a,b,c],[x,y,z] ]
    # return [a+x, b+y, c+z]
    def sum_of_vector_points(self):
        _vectors = map(lambda x: x.co_ords, self.vectors)
        return [sum(i) for i in zip(*_vectors)]

    # calculate centroid of the cluster
    # cluster = [ [a,b,c], [x,y,z], [l,m,n] ]
    # centroid = [ a+x+l / 3, b+y+m / 3, c+z+n / 3  ]
    def calculate_centroid(self):
        centroid = [float(i) / len(self.vectors) for i in self.sum_of_vector_points()]
        self.centroid = numpy.array(centroid)
        return self.centroid
