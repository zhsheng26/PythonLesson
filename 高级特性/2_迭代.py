#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 16:45
# @Author  : zhangsheng


# 只要是可迭代对象，无论有无下标，都可以迭代
from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
# 默认情况下，dict迭代的是key
for key in d:
    print(key)
# 如果要迭代value，可以用for value in d.values()
for value in d.values():
    print(value)
# 如果要同时迭代key和value，可以用for k, v in d.items()
for k, v in d.items():
    print(k, v)

# 如何判断一个对象是可迭代对象呢:通过collections模块的Iterable类型判断

print(isinstance(d, Iterable))
print(isinstance("zhsheng", Iterable))
print(isinstance(98989, Iterable))

# 使用enumerate可以对List进行下标索引循环
for index, value in enumerate(['A', 'B', 'C']):
    print(index, value)

# for循环里，可以同时引用了两个变量
for i, j in [("A", 1), ("B", 2)]:
    print(i, j)
