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
# 要创建一个class对象，type()函数依次传入3个参数：
# 1、class的名称；
# 2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
