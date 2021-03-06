# !/usr/bin/env python
# -*- coding: utf-8 -*-
#  Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 13: Write a function istrcmp to compare two strings, ignoring the case.
"""

def istrcmp(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return s1 == s2

print istrcmp('python', 'Python')
print istrcmp('LaTex', 'Latex')
print istrcmp('a', 'b')

"""
Output:
True
True
False
"""
