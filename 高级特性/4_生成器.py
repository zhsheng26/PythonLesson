#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/14 08:30
# @Author  : zhangsheng


# generator 不必创建完整的list，从而节省大量的空间

# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

g = (x * x for x in range(10))
for value in g:
    print(value)


def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib1(5)


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
# generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 遇到yield语句返回
        a, b = b, a + b
        n = n + 1
    return 'done'


fib_generator = fib2(5)
print(next(fib_generator))
print('=================')
# 用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
for num in fib2(6):
    print(num)
    # 没有打印return语句的返回值 'done'

fib_g = fib2(6)
while True:
    try:
        print('fib_g_vale:', next(fib_g))
    except StopIteration as e:
        print('return value:', e.value)
        break
