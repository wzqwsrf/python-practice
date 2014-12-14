# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月14日15:22:54

"""
Problem 6: Write a program antihtml.py that takes a URL as argument,
downloads the html from web and print it after stripping html tags.
"""

import os
import sys
import urllib
import re


def antihtml():
    url = sys.argv[1]
    u_len = len(url)
    if url[u_len - 1] == '/':
        file_name = 'index.html'
    else:
        url_msg = url.split('/')
        u_len = len(url_msg)
        file_name = url_msg[u_len - 1]
    print 'saving ' + url + ' as ' + file_name
    save_prefix = '/home/zhenqingwang/'
    save_path = os.path.join(save_prefix, file_name)
    urllib.urlretrieve(url, save_path)
    lines = open(save_path).readlines()
    re_h = re.compile('</?\w+[^>]*>')  # HTML标签
    for line in lines:
        print re_h.sub('', line),


antihtml()

"""
Input && Output
$ python wget.py http://docs.python.org/tutorial/interpreter.html
saving http://docs.python.org/tutorial/interpreter.html as interpreter.html.

$ python wget.py http://docs.python.org/tutorial/
saving http://docs.python.org/tutorial/ as index.html.
"""
