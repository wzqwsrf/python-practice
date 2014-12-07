# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年11月29日23:48:14

"""
Problem 21: Write a program wrap.py that takes filename
and width as aruguments and wraps the lines longer than width.
"""

import sys


def wrap():
    file_name = sys.argv[1]
    f_len = int(sys.argv[2])
    real_file = open(file_name)
    lines = real_file.readlines()
    for line in lines:
        line = line.replace('\n', '')
        s_len = len(line)
        if s_len > f_len:
            for i in range(0, s_len, f_len):
                print line[i:(i + f_len)]
        else:
            print line
    real_file.close()


wrap()

"""
Input:
$ cat she.txt
She sells seashells on the seashore;
The shells that she sells are seashells I'm sure.
So if she sells seashells on the seashore,
I'm sure that the shells are seashore shells.

Output:
$ python 21.py she.txt 30
She sells seashells on the sea
shore;
The shells that she sells are
seashells I'm sure.
So if she sells seashells on t
he seashore,
I'm sure that the shells are s
eashore shells.

"""
