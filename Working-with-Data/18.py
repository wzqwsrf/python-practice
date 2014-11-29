# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年11月29日23:30:18

"""
Problem 18: Write a program to print each line of a file in reverse order.
"""

import sys


def reverse_every_line():
    file_name = sys.argv[1]
    lines = open(file_name).readlines()
    for line in lines:
        line = line.replace('\n', '')
        line = line[::-1]
        print line

reverse_every_line()

"""
Input:
$ cat she.txt
She sells seashells on the seashore;
The shells that she sells are seashells I'm sure.
So if she sells seashells on the seashore,
I'm sure that the shells are seashore shells.

Output:
$ python 18.py she.txt
;erohsaes eht no sllehsaes slles ehS
.erus m'I sllehsaes era slles ehs taht sllehs ehT
,erohsaes eht no sllehsaes slles ehs fi oS
.sllehs erohsaes era sllehs eht taht erus m'I
"""
