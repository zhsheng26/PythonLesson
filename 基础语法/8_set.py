#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/12 14:12
# @Author  : zhangsheng

# set 没有重复的元素
# 创建一个set
a_set = {6, 3, 4, 2}
print(isinstance(a_set, set))
# 将list转为set
a_list = [5, 1, 3, 6, 5, 6]
print(a_list)
a_set = set(a_list)  # 重复元素在set中自动被过滤
print(a_set)

s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)  # 交集
print(s1 | s2)  # 并集
# set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等

# 字符串是不可变对象
a_str = 'abc'
b_str = a_str.replace('a', 'A')  # 创建了一个新字符串'Abc'并返回
print(a_str)
print(b_str)
