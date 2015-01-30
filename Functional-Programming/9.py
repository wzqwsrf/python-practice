# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月30日13:01:25

"""
Problem 9: Write a function permute to compute all possible permutations of elements of a given list.
"""


def permute(data):
    """
    >>> permute([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    data.sort()
    result = []
    dLen = len(data)
    visit = [0 for i in range(dLen)]
    dfs(data, visit, dLen, result, [])
    return result


def dfs(data, visit, dLen, result, inResult):
    if len(inResult) == dLen:
        result.append([x for x in inResult])
        return
    for i in xrange(dLen):
        if visit[i] == 0:
            visit[i] = 1
            inResult.append(data[i])
            dfs(data, visit, dLen, result, inResult)
            visit[i] = 0
            inResult.pop()


print permute([1, 2, 3])


"""
Output
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
"""

