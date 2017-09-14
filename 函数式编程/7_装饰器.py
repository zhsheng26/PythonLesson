#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/14 21:23
# @Author  : zhangsheng

# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
import functools


def log(fun):
    def decorator(*args, **kwargs):
        print('执行%s()之前' % fun.__name__)
        return fun(*args, **kwargs)

    return decorator


# 在wrapper()函数内，首先打印日志，再紧接着调用原始函数

@log
def now():
    print('2017-9-14')


# now =  log(now)

now()
print(now.__name__)  # decorator


# 如果decorator本身需要传入参数

def log(text):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            print('输入参数%s' % text, '执行方法%s()之前' % fun.__name__)
            return fun(*args, **kwargs)

        return wrapper

    return decorator


@log("zhangsheng")
def now():
    print('2017-9-14')


# now = log('execute')(now)
now()
print(now.__name__)  # wrapper


########### Python内置的@functools.wraps(fun) ##############
def log(text):
    def decorator(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            print('输入参数%s' % text, '执行方法%s()之前' % fun.__name__)
            return fun(*args, **kwargs)

        return wrapper

    return decorator


@log("zhangsheng")
def now():
    print('2017-9-14')


print(now.__name__)  # now
