#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/14 10:10
# @Author  : zhangsheng


# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。

# 可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator


# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数

# 通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
from collections import Iterator, Iterable

l = [1, 2, 3, 4, 5]
for x in l:
    pass

# 首先获得Iterator对象:
it = iter(l)
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

print(isinstance(l, Iterable))
print(isinstance(l, Iterator))
print(isinstance(it, Iterator))
