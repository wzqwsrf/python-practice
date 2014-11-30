# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年11月30日15:37:01

"""
Problem 23: Write a program center_align.py to center align all lines in the given file.
"""

import sys


def center_align():
    file_name = sys.argv[1]
    lines = open(file_name).readlines()
    max_len = max([len(line) for line in lines])
    for line in lines:
        line = line.replace('\n', '')
        s_len = len(line)
        if s_len < max_len:
            i_len = max_len - s_len
            m_len = i_len / 2
            space = ''
            for i in range(m_len):
                space += ' '
            if i_len % 2 == 0:
                print space + line + space
            else:
                print space + line + space + ' '
        else:
            print line


center_align()

"""
Input:
$ cat she.txt
She sells seashells on the seashore;
The shells that she sells are seashells I'm sure.
So if she sells seashells on the seashore,
I'm sure that the shells are seashore shells.

Output:
$ python 23.py she.txt
I'm sure that the shells are seashore shells.
    So if she sells seashells on the seashore,
The shells that she sells are seashells I'm sure.
       She sells seashells on the seashore;

"""
