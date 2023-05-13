#!/usr/bin/env python3
"""mapper.py"""

import sys
from collections import Counter

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def read_stopwords(file):
    for line in file:
        yield line.strip()

def main():
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    stopwords = read_stopwords(open('stopword.txt', 'r'))
    stop_words = set(stopwords)
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        # word_count = Counter()
        # for word in words:
        #     word = word.lower()
        #     if word not in stop_words:
        #         word_count[word] += 1
        # for word, count in word_count.items():
        #     print ('%s\t%s' % (word, count))
        for word in words:
            word = word.lower()
            if word not in stop_words:
                print ('%s %d' % (word, 1))

if __name__ == "__main__":
    main()
