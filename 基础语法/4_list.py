#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/12 09:33
# @Author  : zhangsheng
# @Site    : 
# @File    : 4_list.py
# @Software: PyCharm


# list是一种有序的集合
classmates = ['Michael', 'Bob', 'Tracy']
# 取最后一个元素:索引-1
print(classmates[-1])
print(classmates[-2])
# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('Adam')
classmates.insert(2, 'Tom')
print(classmates)
# 删除元素
classmates.pop()  # 删除最后一个
print(classmates)
classmates.pop(2)  # 删除指定位置的元素
print(classmates)

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
# list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
