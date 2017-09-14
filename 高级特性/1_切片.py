#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 16:04
# @Author  : zhangsheng


name_list = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前三个name_list[:3]\name_list[0:3]
print(name_list[:3])
# 支持倒数切片
print(name_list[-1])  # Jack
print(name_list[-2:-1])  # ['Bob'] 含头不含尾部

num_list = list(range(100))
print(num_list[-10:])
# 前11-20个数：
print(num_list[10:20])
# 前10个数，每两个取一个：
print(num_list[:10:2])  # [0, 2, 4, 6, 8]
# 所有数，每5个取一个：
print(num_list[::5])
# 倒序
print(num_list[::-1])
# 只写[:]就可以原样复制一个list
print(num_list[:])


# 同样可以对tuple和string进行切片操作，返回的分别是tuple和string
