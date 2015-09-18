__author__ = 'raj'
from sklearn.feature_extraction.text import CountVectorizer
import sys

vectorizer = CountVectorizer(min_df=1)

with open(sys.argv[1]) as f:
    corpus = [line.strip() for line in f]
    vectorizer.fit_transform(corpus)
