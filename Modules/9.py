# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Wangzhenqing <wangzhenqing1008@163.com>
# Date: 2014年12月14日15:48:01

"""
Problem 9: Write a regular expression to validate a phone number.
"""

import re


def validate_phone(phone_no):
    regex = '13[0-9]{9}'
    p = re.compile(regex)
    match = p.match(phone_no)
    if match:
        print match.group(0)
    else:
        print 'phone number is error!'


validate_phone('13709021243')
validate_phone('010')

"""
Output
13709021243
phone number is error!
"""
