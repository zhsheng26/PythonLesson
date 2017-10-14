#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/4 17:55
# @Author  : zhangsheng
import json

import requests

BASE_URL = 'https://api.douban.com/v2/book/2129650'


def req_get_no_param():
    requests_get = requests.get(BASE_URL)
    print('>>> requests headers:')
    print(requests_get.headers)
    print('>>> requests response:')
    print(requests_get.text)


def req_get_use_param():
    params = {'name': 'andy', 'email': 'zhsheng@126.com'}
    response = requests.get(BASE_URL, params=params)
    print(response.reason)


# =========================

GIT_URL = 'https://api.github.com'


def build_url(endpoint):
    return '/'.join([GIT_URL, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=2)


def req_user_git_info():
    response = requests.get(build_url('users/zhsheng26'))
    print(better_print(response.text))


if __name__ == '__main__':
    req_get_no_param()
    req_get_use_param()
    req_user_git_info()

# 表单参数提交
# requests.post('', data={'name': 'andy', 'email': 'zhshsheng@126.com'})
# json参数提交
# requests.post('', json={'name': 'andy', 'email': 'zhshsheng@126.com'})
