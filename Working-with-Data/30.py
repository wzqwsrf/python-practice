# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月07日15:27:29

"""
Problem 30: Write a python function parse_csv to
parse csv (comma separated values) files.
"""


def parse_csv(file_name):
    line = open(file_name).read()
    return [[x for x in y.split(',')] for y in line.split('\n')]

print parse_csv('a.csv')

"""
Input:
$ print open('a.csv').read()
a,b,c
1,2,3
2,3,4
3,4,5

Output:
[['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]
"""
