# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月23日11:50:34

"""
Iterators Test2
"""

if __name__ == '__main__':
    x = iter([1, 2, 3])
    print x
    print x.next()
    print x.next()
    print x.next()
    print x.next()

"""
Output
<listiterator object at 0x10b8719d0>
Traceback (most recent call last):
1
  File "/Users/wzqwsrf/git_work/python-practice/Iterators-Generators/t-2.py", line 16, in <module>
2
    print x.next()
3
StopIteration
"""
