#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/14 12:04
# @Author  : zhangsheng


# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
print(list(filter(lambda x: x % 2 == 0, range(10))))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# 结果: ['A', 'B', 'C']
# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 回数
def is_palindrome(n):
    return int(str(n)[::-1]) == n


output = filter(is_palindrome, range(1, 100))
print(list(output))
