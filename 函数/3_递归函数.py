#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/13 15:27
# @Author  : zhangsheng


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# 递归调用的次数过多，会导致栈溢出

# 解决递归调用栈溢出的方法是通过尾递归优化

# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact(5))
# 大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出
