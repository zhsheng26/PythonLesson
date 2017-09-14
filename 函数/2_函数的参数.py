#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/12 16:58
# @Author  : zhangsheng


# ################位置参数
# power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n
def power1(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power1(5, 2))
print(power1(5, 3))


# ################默认参数
def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 必选参数在前，默认参数在后;
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

print(power2(5))
print(power2(5, 3))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


print('-----------')
enroll('andy', 'F')
print('-----------')
enroll('andy', 'F', 8)
print('-----------')
enroll('andy', 'F', city='hefei')


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=[]):  # 默认参数L也是一个变量，它指向对象[]
    L.append('END')
    return L


print(add_end([1, 4, 5]))  # [1, 4, 5, 'END']
print(add_end())  # ['END']
print(add_end())  # ['END', 'END'] 错误


def append_end(l=None):
    if l is None:
        l = []
    l.append('END')
    return l


print(append_end())
print(append_end())


# ############################可变参数
# 仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
# 允许在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1, 2, 3]
print(calc(*nums))


# ############################关键字参数
# 关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 可以只传入必选参数
person('andy', 12)
# 也可以传入任意个数的关键字参数
person('Tom', 18, grade='一年级', job='Engineer')  # name: Tom age: 18 other: {'grade': '一年级', 'job': 'Engineer'}
# 也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Lady', 12, **extra)  # kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


# ############################命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数,命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person1(name, age, *, city, job):
    print(name, age, city, job)


person1('Lily', 23, city='hefei', job='teacher')


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# person1('Lily', 23)#运行将报错

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数可以有缺省值，从而简化调用
def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person3('KiKi', 24, job="teacher")  # KiKi 24 Beijing teacher

# 组合参数
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
# *args是可变参数，args接收的是一个tuple
# **kw是关键字参数，kw接收的是一个dict
