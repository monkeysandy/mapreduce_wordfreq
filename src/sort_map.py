#!/usr/bin/env python3
"""used to sort the output of multiple reducers"""

import sys
from collections import Counter

for line in sys.stdin:
    line = line.strip()
    # if line:
    #     word, count = line.split('\t')
    #     print ('%s\t%s' % (word, count))
    if line:
        word = line.split()[0]
        count = line.split()[1]
        print ('%s\t%s' % (word, count))