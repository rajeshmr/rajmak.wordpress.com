__author__ = 'raj'

from utils import euclidean_distance


class Cluster:
    def __init__(self, _cid, _initial_vector):
        self.cid = _cid
        self.vectors = {_initial_vector}
        self.centroid = self.calculate_centroid()

    def __repr__(self):
        out = ["cluster-id: %d vector-id %d: distance from centroid %f" % (
            self.cid, v.vid, euclidean_distance(v.co_ords, self.centroid)) for v in self.vectors]
        return "\n".join(out)

    def add_vector_to_cluster(self, _vector):
        _vector.set_distance_from_centroid(self.centroid)
        self.vectors.add(_vector)
        return ",".join(map(str, self.calculate_centroid()))

    def sum_of_vector_points(self):
        _vectors = map(lambda x: x.co_ords, self.vectors)
        return [sum(i) for i in zip(*_vectors)]

    def calculate_centroid(self):
        self.centroid = [float(i) / len(self.vectors) for i in self.sum_of_vector_points()]
        return self.centroid
