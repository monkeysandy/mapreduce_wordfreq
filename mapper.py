#!/usr/bin/env python3
"""mapper.py"""

import sys

stop_words = set(line.strip() for line in open('stopword.txt'))

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        word = word.lower()
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if word not in stop_words:
            print ('%s\t%s' % (word, 1))
