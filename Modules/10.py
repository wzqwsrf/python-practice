# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2015年01月20日09:36:45

"""
Problem 10: Write a program myip.py to print the external IP address of the machine.
Use the response from http://httpbin.org/get and read the IP address from there.
The program should print only the IP address and nothing else.
"""

import urllib2
import json


def myip():
    url = 'http://httpbin.org/get'
    res = urllib2.urlopen(url)
    json_date = res.read()
    json_date = json.loads(json_date)
    print type(json_date)
    return json_date['origin']


print myip()

"""
Output
61.135.207.197
"""
