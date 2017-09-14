#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/14 11:02
# @Author  : zhangsheng

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
from collections import Iterator
from functools import reduce

list_num = list(range(10))


def fun(x):
    return x * x


num_iter = map(fun, list_num)
print(isinstance(num_iter, Iterator))
for num in num_iter:
    print(num)

# reduce 把一个接收两个参数的函数作用在一个序列，reduce把结果继续和序列的下一个元素做累积计算
print("求和：", reduce(lambda x, y: x + y, range(5)))


# str2int

def str2int(str_num):
    def trans_num(ch):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[ch]

    return reduce(lambda x, y: x * 10 + y, map(trans_num, str_num))


print(isinstance(str2int('1234'), int))
