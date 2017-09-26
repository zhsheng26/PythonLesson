#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/22 14:59
# @Author  : zhangsheng
import logging

try:
    print('try...')
    r = 10 / int('0')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


# foo('0')


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


# bar()

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型

logging.basicConfig(level=logging.INFO)
# 指定记录信息的级别，有debug，info，warning，error
s = '1'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
