#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/24 17:53
# @Author  : zhangsheng

import os

print(os.name)
print(os.uname())

print(os.environ)
print(os.environ.get('PYTHONPATH'))
print(os.environ.get('x', 'default'))
