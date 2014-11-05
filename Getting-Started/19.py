# -*- coding: utf-8 -*-
"""
Problem 19: Write a program add.py that takes 2 numbers as command line arguments and prints its sum.
"""

import sys

def add():
    s_len = len(sys.argv)
    sum = 0
    for i in range(1, s_len):
        sum += int(sys.argv[i])
    return sum

print add()

"""
Output:
根据输入参数值变化，可以传入多个参数，不止２个
执行
python 19.py 3 5
"""
