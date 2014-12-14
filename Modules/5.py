# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月14日15:12:47

"""
Problem 5: Write a program wget.py to download a given URL.
The program should accept a URL as argument, download it and
save it with the basename of the URL. If the URL ends with a /,
consider the basename as index.html.
"""

import os
import sys
import urllib


def wget():
    url = sys.argv[1]
    u_len = len(url)
    if url[u_len-1] == '/':
        file_name = 'index.html'
    else:
        url_msg = url.split('/')
        u_len = len(url_msg)
        file_name = url_msg[u_len-1]
    print 'saving ' + url + ' as ' + file_name
    urllib.urlretrieve(url, os.path.join('/home/zhenqingwang/', file_name))

wget()

"""
Input && Output
$ python wget.py http://docs.python.org/tutorial/interpreter.html
saving http://docs.python.org/tutorial/interpreter.html as interpreter.html.

$ python wget.py http://docs.python.org/tutorial/
saving http://docs.python.org/tutorial/ as index.html.
"""
