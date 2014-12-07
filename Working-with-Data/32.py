# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月07日15:47:02

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
    # del
    words = []
    for s in word:
        words.append(str(word).replace(s, ''))
    #   insert
    for i in range(d_len):
        for x in range('a', 'z' + 1):
            words.append(word[0, i] + x + word[i, d_len])
#   replace
    for s in word:
        for x in range('a', 'z' + 1):
            words.append(str(word).replace(s, str(x)))
#   swap
    for i in range(d_len-1):
        s = word[i]
        e = word[i+1]
        words.append(str(word).replace())

"""
Input:
$ print open('a.txt').read()
# elements are separated by ! and comment indicator is #
a!b!c
1!2!3
2!3!4
3!4!5

Output:
[['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]
"""
