#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/14 21:52
# @Author  : zhangsheng
import functools


def int2(x, base=2):
    return int(x, base)


# 转换二进制
print(int2('1000000'))

# functools.partial创建一个偏函数

# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

int3 = functools.partial(int, base=2)  # 固定了int()函数的关键字参数base

print(int3('1000000'))
# 相当于
kw = {'base': 2}
print(int('1000000', **kw))

max2 = functools.partial(max, 10)  # 把10作为*args的一部分自动加到左边
print(max2(1, 2, 4, 5))  # 10
