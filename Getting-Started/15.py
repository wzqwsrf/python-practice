# -*- coding: utf-8 -*-
"""
Problem 15: What will be output of the following program?
"""

x = 4
y = 5
p = x < y and x < z
print p

"""
Output:
True
虽然z没有定义，但是or只要前者为True,就不判断后者了。
可以测试一下 p = x < y and x < z
报错：NameError: name 'z' is not defined
"""
