# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月07日18:20:28

"""
Problem 32: Write a function mutate to compute all words generated
by a single mutation on a given word.
A mutation is defined as inserting a character,
deleting a character, replacing a character, or swapping
2 consecutive characters in a string.
For simplicity consider only letters from a to z.
"""


def mutate(word):
    d_len = len(word)
    words = []
    d_word = word
    start = ord('a')
    end = ord('z') + 1
    for i in range(d_len):
        if i < d_len - 1:
            # swap
            words.append(d_word[:i] + d_word[i + 1] + d_word[i] + d_word[i + 2:])
        for x in range(start, end):
            x = chr(x)
            # insert
            words.append(d_word[:i] + x + d_word[i:])
            # del
            words.append(d_word[:i] + d_word[i + 1:])
            # replace
            words.append(d_word[:i] + x + d_word[i + 1:])
    return words

words = mutate('hello')
print 'helo' in words
print 'cello' in words
print 'helol' in words

"""
Output:
True
True
True
"""
