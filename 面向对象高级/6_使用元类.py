#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/19 08:58
# @Author  : zhangsheng


# type()函数可以查看一个类型或变量的类型


class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


h = Hello()
# Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello
print(type(h))
print(type(Hello))


# 通过type()函数创建出Hello类

def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
