__author__ = 'raj'
import re
from random import randint
from kmeans import KMeans
import numpy
from metaphone import doublemetaphone



class Mapper:
    def __init__(self):
        self.words = set()
        self.k = int(self.params.get("k", "10"))
        self.bag_of_words = open("resources/bag_of_words.txt", "r")
        self.words = set([word.strip() for word in self.bag_of_words])

    def __call__(self, key, title):
        vector = []
        title = re.sub(r"[^a-zA-Z]", " ", title).lower()
        words_in_title = map(lambda x: x.strip(), title.split())
        words_in_title = filter(lambda x: len(x) > 2, words_in_title)
        for word in self.words:
            count = len(filter(lambda x: x in word, words_in_title))
            vector.append(float(count))
        yield randint(0, self.k), vector


class Reducer:
    def __init__(self):
        self.k = int(self.params.get("k", "10"))
        self.max_iterations = int(self.params.get("max_iterations", "100"))
        self.kmeans = KMeans(self.k, self.max_iterations)

    def __call__(self, key, values):
        # convert input to numpy_array and feed the vectors to KMeans instance
        for _vid, _vector_array in enumerate(values):
            _vector_array = numpy.array(_vector_array)
            self.kmeans.add_vector(_vid, _vector_array)
        self.kmeans.initialize()

        for _cluster in self.kmeans.run():
            for item in _cluster:
                yield item.cid, item

if __name__ == "__main__":
    import dumbo
    dumbo.run(Mapper, Reducer)
