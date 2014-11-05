# -*- coding: utf-8 -*-
"""
Problem 8: What will be the output of the following program?
"""
x = 1
def f():
    return x
print x
print f()

"""
Output:
1
1
内部函数访问全局变量
"""
