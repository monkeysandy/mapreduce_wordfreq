#!/usr/bin/env python3

import sys

data = []

for line in sys.stdin:
    line = line.strip()
    if line:
        word, count = line.split('\t')
        data.append((word, int(count)))

data.sort(key=lambda x: x[1], reverse=True)

for word, count in data[:100]:
    print ('%s\t%s' % (word, count))