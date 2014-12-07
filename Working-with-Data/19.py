# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年11月29日23:33:02

"""
Problem 19: Implement unix commands head and tail.
The head and tail commands take a file as argument
and prints its first and last 10 lines of the file respectively.
"""

import sys


def head():
    file_name = sys.argv[1]
    real_file = open(file_name)
    lines = real_file.readlines()
    num = 0
    for line in lines:
        if num >= 10:
            continue
        num += 1
        line = line.replace('\n', '')
        print line
    real_file.close()


def tail():
    file_name = sys.argv[1]
    real_file = open(file_name)
    lines = real_file.readlines()
    lines.reverse()
    num = 0
    for line in lines:
        if num >= 10:
            continue
        num += 1
        line = line.replace('\n', '')
        print line
    real_file.close()

head()
tail()

"""
Input:
$ cat file.txt

Output:
$ python 19.py file.txt
Between persons of equal income there is no social distinction
except the distinction of merit.
Money is nothing;
character, conduct, and capacity are everything.
Instead of all the workers being leveled
down to low wage standards and all the rich
leveled up to fashionbale income standards,
everybody under a system of equal incomes would
find his or her own natural level.
There would be great people and ordinary people and little peolpe,


and the really great in favour of equality.
(their only chance of eminence),
That is why idiots are always in favour of inequality of income
and not poor persons who had never had a chance.
and the little would be persons of small minds and mean characters,
and whose father had left a hunred thousand a year;
and never the idiot whose mother had spoiled them
but the great would always be those who had done great things,
There would be great people and ordinary people and little peolpe,
find his or her own natural level.

"""
