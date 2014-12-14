# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月14日15:55:23

"""
Problem 8: Write a program links.py that takes URL of a webpage
as argument and prints all the URLs linked from that webpage.
"""

import re
import sys


def links():
    dir_name = sys.argv[1]
    lines = open(dir_name).readlines()
    p = re.compile('^[a-zA-z]+://(\w+(-\w+)*)(\.(\w+(-\w+)*))*(\?\S*)?$',re.S)
    for line in lines:
        print line
        m = p.match(line)
        if m:
            print m.group(1)
        # else:
            # print "aaa"

links()

"""
Output
hello-world
hello-world
hello-world
"""
