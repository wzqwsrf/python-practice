# -*- coding: utf-8 -*-
"""
Problem 9: What will be the output of the following program?
"""
x = 1
def f():
    x = 2
    return x
print x
print f()
print x

"""
Output:
1
2
1
在函数内部ｘ为局部变量，所以其实是声明了一个局部变量，而不是修改全局变量
"""
