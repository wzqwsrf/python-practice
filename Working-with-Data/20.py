# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年11月29日23:41:47

"""
Problem 20: Implement unix command grep.
The grep command takes a string and a file as arguments
and prints all lines in the file which contain the specified string.
"""

import sys


def grep():
    file_name = sys.argv[1]
    in_str = sys.argv[2]
    real_file = open(file_name)
    lines = real_file.readlines()
    for line in lines:
        line = line.replace('\n', '')
        if in_str not in line:
            continue
        print line
    real_file.close()

grep()

"""
Input:
$ cat she.txt
She sells seashells on the seashore;
The shells that she sells are seashells I'm sure.
So if she sells seashells on the seashore,
I'm sure that the shells are seashore shells.

Output:
$ python 20.py she.txt sure
The shells that she sells are seashells I'm sure.
I'm sure that the shells are seashore shells.

"""
