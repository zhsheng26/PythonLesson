#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 10:13
# @Author  : zhangsheng
import itertools

# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算
# count()会创建一个无限的迭代器
itertools_count = itertools.count(1)
take_nums = itertools.takewhile(lambda x: x < 10, itertools_count)
print(list(take_nums))

# cycle repeat
ns = itertools.repeat('A', 3)
for st in ns:
    print(st)
# chain
for ch in itertools.chain('abc', 'xyz'):
    print(str.upper(ch))

# groupBy
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
for key, group in itertools.groupby(sorted('AAABBBCCAAA')):
    print(key, list(group))
