#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/19 08:41
# @Author  : zhangsheng

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)  # value属性则是自动赋给成员的int常量，默认从1开始计数。


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Mon)
print(Weekday.Mon.value)

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
