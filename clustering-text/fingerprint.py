import re
import string

import nltk
from nltk import bigrams
from stemming.porter2 import stem


class FingerPrint(object):
    def __init__(self):
        super(FingerPrint, self).__init__()
        self.remove_spl_char_regex = re.compile(
            '[%s]' % re.escape(string.punctuation))  # regex to remove special characters
        self.remove_num = re.compile('[\d]+')

    def fp_steps(self, text):
        title = text.strip().lower()
        title_splchar_removed = self.remove_spl_char_regex.sub(" ", title)
        title_number_removed = self.remove_num.sub("", title_splchar_removed)
        words = title_number_removed.split()
        filter_stop_words = [w for w in words if not w in nltk.corpus.stopwords.words('english')]
        stemed = [stem(w) for w in filter_stop_words]
        return sorted(stemed)

    def fingerprint(self, text):
        fp = " ".join(self.fp_steps(text))
        return fp

    def bigram_fingerprint(self, text):
        fp = self.fingerprint(text)
        bigram = bigrams(fp.replace(" ", ""))
        b = []
        for bi in bigram:
            b.append("".join(bi))
        return "".join(sorted(set(b)))
