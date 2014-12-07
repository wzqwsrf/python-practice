# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年11月30日23:16:39

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
    real_file = open(file_name)
    lines = real_file.readlines()
    for line in lines:
        line = line.replace('\n', '')
        s_len = len(line)
        line_msg = line.split(' ')
        e_len = len(line_msg)
        if s_len > f_len:
            dic = {}
            for i in range(e_len):
                dic[i] = line_msg[i]
            i_len = 0
            in_line = ''
            for i in range(e_len):
                t_len = i_len + len(dic[i])
                if t_len > f_len:
                    print in_line
                    i_len = 0
                    in_line = ''
                i_len += len(dic[i]) + 1
                in_line += (dic[i] + ' ')
                if i == e_len - 1:
                    print in_line
        else:
            print line
    real_file.close()


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
She sells seashells on the
seashore;
The shells that she sells are
seashells I'm sure.
So if she sells seashells on
the seashore,
I'm sure that the shells are
seashore shells.

"""
