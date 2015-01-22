# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月22日11:41:27

"""
Problem 2: What will the output of the following program.
"""


try:
    print "a"
except:
    print 'b'
else:
    print "c"
finally:
    print "d"


"""
Output
a
c
d
"""
