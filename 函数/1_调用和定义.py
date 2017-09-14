#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/12 15:54
# @Author  : zhangsheng


# 内置函数
import math

abs(-90)
print(max(2, 4, 13, 19))
# 类型转换函数 int() 、float() 、str(100)、 bool(1)
a_str = str(0.33)
print(isinstance(a_str, str))  # true
print(bool(1))
print(bool(''))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
my_abs = abs
print(my_abs(-999))


# 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
def print_your_name(name):
    print('your name %s' % name)


print_your_name('zhangsheng')

# pass
age = 199
if age > 10:
    pass


# 函数可以返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
# Python的函数返回多值其实就是返回一个tuple，在语法上，返回一个tuple可以省略括号,写起来更方便。
step = move(100, 100, 60, math.pi / 6)
print(step)
