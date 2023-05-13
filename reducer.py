#!/usr/bin/env python3
"""reducer.py"""

import sys
from collections import defaultdict
from heapq import nlargest

# current_word = None
# current_count = 0
# word = None
# count_dict = defaultdict(int)

# # input comes from STDIN
# for line in sys.stdin:
#     # remove leading and trailing whitespace
#     line = line.strip()

#     # parse the input we got from mapper.py
#     word, count = line.split('\t', 1)

#     # convert count (currently a string) to int
#     try:
#         count = int(count)
#     except ValueError:
#         # count was not a number, so silently
#         # ignore/discard this line
#         continue

#     # this IF-switch only works because Hadoop sorts map output
#     # by key (here: word) before it is passed to the reducer
#     if current_word == word:
#         current_count += count
#     else:
#         if current_word:
#             count_dict[current_word] += current_count
#         current_count = count
#         current_word = word

# # do not forget to output the last word if needed!
# if current_word == word:
#     count_dict[current_word] += current_count

# # Get the top 10 words
# top_10_words = nlargest(10, count_dict.items(), key=lambda x: x[1])

# # write the results to STDOUT
# for word, count in top_10_words:
#     print('%s\t%s' % (word, count))


def read_mapper_output(file, separator=' '):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator=' '):
    data = read_mapper_output(sys.stdin, separator=separator)
    count_dict = defaultdict(int)
    for word, count in data:
        count_dict[word] += int(count)
    top_100_words = nlargest(100, count_dict.items(), key=lambda x: x[1])
    for word, count in top_100_words:
        # print('%s\t%s' % (word, count))
        print('{:<15} {:<10}'.format(word, count))

if __name__ == "__main__":
    main()