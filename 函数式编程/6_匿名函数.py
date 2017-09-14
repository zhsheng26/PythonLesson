#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/14 21:17
# @Author  : zhangsheng

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
# 也可以把匿名函数作为返回值返回


def num_sum(x, y):
    return lambda: x * x + y * y
