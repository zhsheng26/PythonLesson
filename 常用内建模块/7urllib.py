#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 14:27
# @Author  : zhangsheng

from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    data = f.read()
    print('Data:', data.decode('utf-8'))
print('===========================')
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# <meta name="viewport" content="width=device-width, height=device-height, user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0">
# <meta name="format-detection" content="telephone=no">
