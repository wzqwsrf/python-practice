# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年11月29日23:20:46

"""
Problem 17: Write a program reverse.py to print lines of a file in reverse order.
"""

def reverse():
    lines = open('she.txt').readlines()
    lines.reverse()
    for line in lines:
        line = line.replace('\n', '')
        print line

reverse()

"""
Input:
$ cat she.txt
She sells seashells on the seashore;
The shells that she sells are seashells I'm sure.
So if she sells seashells on the seashore,
I'm sure that the shells are seashore shells.

Output:
$ python 17.py she.txt
I'm sure that the shells are seashore shells.
So if she sells seashells on the seashore,
The shells that she sells are seashells I'm sure.
She sells seashells on the seashore;
"""
