# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月21日09:30:07

"""
Problem 11: Write a python program zip.py to create a zip file.
The program should take name of zip file as first argument and files to add as rest of the arguments.
"""

import sys
import zipfile


def zip_new():
    zip_name = sys.argv[1]
    s_len = len(sys.argv)
    print zip_name
    z = zipfile.ZipFile(zip_name, 'w')
    for i in range(2, s_len):
        z.write(sys.argv[i])
    z.close()
    z = zipfile.ZipFile(zip_name)
    for name in z.namelist():
        print name

zip_new()

"""
Output
foo.zip
9.py
10.py
"""
