#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/14 18:14
# @Author  : zhangsheng

list_num = [36, 5, -12, 9, -21]
l1 = sorted(list_num)
print(l1)
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
l2 = sorted([36, 5, -12, 9, -21], key=abs)
print(l2)

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return sorted(t, key=lambda x: x[0])


def by_score(t):
    return sorted(t, key=lambda x: x[1], reverse=True)


print(by_name(L))
print(by_score(L))
