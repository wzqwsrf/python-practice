# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月08日12:30:15

"""
Problem 34: Improve the above program to print the words in the descending order of the number of occurrences.
"""


def word_frequency(words):
    """Returns frequency of each word given a list of words.

        # >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
    """
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency


def read_words(filename):
    return open(filename).read().split()


def main(filename):
    frequency = word_frequency(read_words(filename))
    for word, count in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
        print word, count


if __name__ == "__main__":
    import sys

    main(sys.argv[1])

"""
Input:
$ python 34.py b.txt
Output:
a 3
b 3
c 2
"""
