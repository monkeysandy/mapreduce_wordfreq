#!/usr/bin/env python3
"""combiner.py"""

import sys
from collections import defaultdict

def combine_counts(data):
    count_dict = defaultdict(int)
    for word, count in data:
        count_dict[word] += int(count)
    return count_dict.items()

def read_mapper_output(file, separator=' '):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator=' '):
    data = read_mapper_output(sys.stdin, separator=separator)
    combined_counts = combine_counts(data)
    for word, count in combined_counts:
        print('%s %s' % (word, count))

if __name__ == "__main__":
    main()
