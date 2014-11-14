# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 5: Write a function factorial to compute factorial of a number.
Can you use the product function defined in the previous example to compute factorial?
"""

def factorial(num):
    result = 1
    for x in range(num):
        x = x + 1
        result *= x
    return result

print factorial(4)
print factorial(5)

"""
Output:
24
120
"""
