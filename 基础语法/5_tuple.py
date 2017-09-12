#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/12 11:13
# @Author  : zhangsheng
# @Site    : 
# @File    : 5_tuple.py
# @Software: PyCharm

# tuple 元组，是有序的列表，一旦初始化，不能修改

classmates = ('Michael', 'Bob', 'Tracy')
# 没有append()，insert()这样的方法
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。


# 定义一个空的tuple，可以写成()
# 定义一个只有1个元素的tuple
t = ('name',)
print(len(t))

##############“指向不变”###############
# 特殊的"可变"tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
# 其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list
# 即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
