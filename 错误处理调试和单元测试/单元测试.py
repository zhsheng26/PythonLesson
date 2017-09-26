#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/22 16:44
# @Author  : zhangsheng


class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

# setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
