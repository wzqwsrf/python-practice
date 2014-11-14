# !/usr/bin/env python
# -*- coding: utf-8 -*-
#  Author: Wangzhenqing <wangzhenqing1008@163.com>

"""
Problem 18: What happens when the following code is executed? Will it give any error? Explain the reasons.
"""

x = 2
if x == 2:
    print x
else:
    x +

"""
Output:
 File "18.py", line 9
     x +
       ^
SyntaxError: invalid syntax
报错，代码语法错误，编译的时候校验
"""
