import sys
import nltk

for line in sys.stdin:
    tokens = nltk.word_tokenize(line.strip())
    tagged_tokens = nltk.pos_tag(tokens)
    for token in tagged_tokens:
        print "%s\t%s" % token
