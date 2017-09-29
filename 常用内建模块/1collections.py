#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/27 21:18
# @Author  : zhangsheng

# namedtuple

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性
Circle = namedtuple('Circle', ['x', 'y', 'r'])
circle = Circle(2, 2, 1)
print(circle.r)
# deque 为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

de = deque(['a', 'b', 'c'])
de.appendleft('x')
de.appendleft('y')
print(de)
de.popleft()
print(de)

# defaultdict 如果希望key不存在时，返回一个默认值

default_d = defaultdict(lambda: 'no value')
default_d['key1'] = 'hello'
print(default_d['key1'])
print(default_d['key2'])

# OrderedDict 如果要保持Key的顺序

d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 3)])
print(d)
od = OrderedDict([('a', 1), ('c', 3), ('b', 2)])  # OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
print(od)

# Counter

c = Counter()
for ch in 'program':
    c[ch] = c[ch] + 1
print(c)
