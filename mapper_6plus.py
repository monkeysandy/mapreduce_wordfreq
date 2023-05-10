#!/usr/bin/env python3
"""mapper.py"""

import sys
from collections import Counter

# stop_words = set(line.strip() for line in open('stopword.txt'))

# # input comes from STDIN (standard input)
# for line in sys.stdin:
#     # remove leading and trailing whitespace
#     line = line.strip()
#     # split the line into words
#     words = line.split()
#     # increase counters
#     word_count = Counter()
#     for word in words:
#         word = word.lower()
#         # write the results to STDOUT (standard output);
#         # what we output here will be the input for the
#         # Reduce step, i.e. the input for reducer.py
#         #
#         # tab-delimited; the trivial word count is 1
#         if word not in stop_words:
#             # print ('%s\t%s' % (word, 1))
#             word_count[word] += 1
#     for word, count in word_count.items():
#         print ('%s\t%s' % (word, count))

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def read_stopwords(file):
    for line in file:
        yield line.strip()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    stopwords = read_stopwords(open('stopword.txt', 'r'))
    stop_words = set(stopwords)
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        word_count = Counter()
        for word in words:
            word = word.lower()
            if word not in stop_words and len(word) > 6:
                word_count[word] += 1
        for word, count in word_count.items():
            print ('%s\t%s' % (word, count))

if __name__ == "__main__":
    main()
