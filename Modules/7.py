# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月14日15:48:01

"""
Problem 7: Write a function make_slug that takes a name converts it into a slug.
A slug is a string where spaces and special characters are replaced by a hyphen,
typically used to create blog post URL from post title. It should also make sure
there are no more than one hyphen in any place and there are no hyphens at the
beginning and end of the slug.
"""

from string import strip, punctuation
import re


def make_slug(in_str):
    for x in punctuation:
        in_str = in_str.replace(x, ' ')
    in_str = strip(in_str, ' ')
    in_str = re.sub(' +', ' ', in_str)
    in_str = re.sub(' ', '-', in_str)
    print in_str


make_slug("hello world")
make_slug("hello  world!")
make_slug(" --hello-  world--")

"""
Output
hello-world
hello-world
hello-world
"""
