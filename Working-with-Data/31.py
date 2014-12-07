# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月07日15:42:54

"""
Problem 31: Generalize the above implementation of csv parser
to support any delimiter and comments.
"""


def parse_csv(file_name, split, comment):
    line = open(file_name).read()
    return [[x for x in y.split(split)] for y in line.split('\n') if comment not in y]

print parse_csv('a.txt', '!', '#')

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
