#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 09:05
# @Author  : zhangsheng

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

db = {}


def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')


def get_md5(str_p):
    md_str = hashlib.md5()
    md_str.update(str_p.encode('utf-8'))
    return md_str.hexdigest()


register('andy', 'hello')

print(db)
