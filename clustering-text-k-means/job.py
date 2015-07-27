__author__ = 'raj'
import re
from random import randint
from kmeans import KMeans
import numpy


class Mapper:
    def __init__(self):
        self.words = set()
        self.k = int(self.k) if self.params["k"] else 10
        for word in open("resources/bag_of_words.txt").readlines():
            self.words.add(word.strip())

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
        self.k = int(self.param["k"])
        self.max_iterations = int(self.param["max_iterations"])
        self.kmeans = KMeans(self.k, self.max_iterations)

    def __call__(self, key, values):
        # convert input to numpy_array and feed the vectors to KMeans instance
        for _vid, _vector_array in enumerate(values):
            _vector_array = eval(_vector_array) # string to array
            _vector_array = numpy.array(_vector_array) # array to numpy_array
            self.kmeans.add_vector(_vid, _vector_array)
        self.kmeans.initialize()

        for _cluster in self.kmeans.run():
            print _cluster
            print


if __name__ == "__main__":
    import dumbo
    dumbo.run(Mapper, Reducer)
