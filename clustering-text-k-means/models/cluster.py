__author__ = 'raj'
import numpy

class Cluster:
    def __init__(self, _initial_vector):
        self.vectors = {_initial_vector}
        self.centroid = self.calculate_centroid()
        self.cid = self.centroid.__hash__()

    def __repr__(self):
        out = ["%d\t%d\t%f" % (self.cid, v.vid, v.get_distance_from_centroid(self.centroid)) for v
               in self.vectors]
        return "\n".join(out)

    def remove(self, vector):
        self.vectors.remove(vector)

    def add_vector_to_cluster(self, _vector):
        _vector.set_distance_from_centroid(self.centroid)
        self.vectors.add(_vector)
        return ",".join(map(str, self.calculate_centroid()))

    def sum_of_vector_points(self):
        _vectors = map(lambda x: x.co_ords, self.vectors)
        return [sum(i) for i in zip(*_vectors)]

    def calculate_centroid(self):
        centroid = [float(i) / len(self.vectors) for i in self.sum_of_vector_points()]
        self.centroid = numpy.array(centroid)
        return self.centroid
