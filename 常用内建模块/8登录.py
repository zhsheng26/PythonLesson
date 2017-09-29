#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 15:19
# @Author  : zhangsheng

from urllib import request, parse

import requests

print('Login to time oa...')
login_data = parse.urlencode([
    ('email', 'zhangsheng@timefac.cn'),
    ('password', 'MTExMTEx'),
])

req = request.Request('http://oa.v5time.net/tfoa/auth/login')
req.add_header('Origin', 'http://oa.v5time.net')
req.add_header('Host', 'oa.v5time.net')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer',
               'http://oa.v5time.net/tfoa/auth')

# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

# with request.urlopen(req, login_data) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

#
# with request.urlopen('http://oa.v5time.net/tfoa/auth/login?email=zhangsheng@timeface.cn&password=MTExMTEx') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

url = 'http://oa.v5time.net/tfoa/auth/login'
login_param = {'email': 'zhangsheng@timeface.cn', 'password': 'MTExMTEx'}
r = requests.get(url, params=login_param)
print(r.status_code)
print(r.headers)
print(r.text)
