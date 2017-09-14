#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 17:45
# @Author  : zhangsheng


print(list(range(1, 11)))
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])  # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + "=" + v for k, v in d.items()])

L = ['XiaoMi', 'HuaWei', 18, 'Apple', None]
print([banner.lower() for banner in L if isinstance(banner, str)])
