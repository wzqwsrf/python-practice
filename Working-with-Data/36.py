# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月08日14:31:54

"""
Problem 36: Write a program to find anagrams in a given list of words.
Two words are called anagrams if one word can be formed by rearranging letters of another.
For example ‘eat’, ‘ate’ and ‘tea’ are anagrams.
"""


def anagrams(in_list):
    dic = {}
    for x in in_list:
        y = x
        x = list(x)
        x.sort()
        x = ''.join(x)
        ou_list = dic.get(x, [])
        ou_list.append(y)
        dic[x] = ou_list
    r_list = []
    for k, v in dic.items():
        r_list.append(v)
    return r_list

print anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])


"""
Output:
[['done', 'node'], ['eat', 'ate', 'tea'], ['soup']]
"""
