#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/14 10:52
# @Author  : zhangsheng


# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# 函数名其实就是指向函数的变量

# 由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。

# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)


print(add(2, -3, abs))
