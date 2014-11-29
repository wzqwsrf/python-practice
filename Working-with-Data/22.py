# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年11月29日23:55:25

"""
Problem 22: The above wrap program is not so nice
because it is breaking the line at middle of any word.
Can you write a new program wordwrap.py that works like wrap.py,
but breaks the line only at the word boundaries?
"""

import sys


def wordwrap():
    file_name = sys.argv[1]
    f_len = int(sys.argv[2])
    lines = open(file_name).readlines()
    for line in lines:
        s_len = len(line)
        line = line.replace('\n', '')
        if s_len > f_len:
            for i in range(0, s_len, f_len):
                print line[i:(i + f_len)]
        else:
            print line


wordwrap()

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
