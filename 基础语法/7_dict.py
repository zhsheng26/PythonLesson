#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/12 11:56
# @Author  : zhangsheng


# dict 使用键-值（key-value）存储，具有极快的查找速度

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d.__setitem__('Tom', 22)
print(d)
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Michael'] = 66
print(d)

# 一是通过in判断key是否存在：
print('Andy' in d)
# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Andy'))
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop("Bob")
print(d)
# dict内部存放的顺序和key放入的顺序是没有关系的

# ###############dict的key必须是不可变对象################
# 因为dict根据key来计算value的存储位置
# 在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key
