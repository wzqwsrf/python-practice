# -*- coding: utf-8 -*-
"""
Problem 10: What will be the output of the following program?
"""
x = 1
def f():
    y = x
    x = 2
    return x + y
print x
print f()
print x

"""
Output: UnboundLocalError: local variable 'x' referenced before assignment
x被认为是局部变量，没有声明就使用，在ｙ＝ｘ之前加上一行 global x 就正常了。
"""
