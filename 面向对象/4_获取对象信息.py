#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/18 11:30
# @Author  : zhangsheng


# 判断对象类型，使用type()函数：返回对应的Class类型
import types

print(type('abc') == type('123'))


def fun():
    pass


print(type(fun) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 对于class的继承关系来说,可以使用isinstance()函数。

# 能用type()判断的基本类型也可以用isinstance()判断：
print(isinstance(b'a', bytes))

# 使用dir(),获取一个对象的所有属性和方法
print(dir('hello'))


# 在len()函数内部，它自动去调用该对象的__len__()方法

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.score = score

    def __len__(self):
        return len(self.__name)

    def get_score(self):
        return self.score


a_stu = Student('Andy', 99)
print(len(a_stu))
print(a_stu.__len__())

# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

print(hasattr(a_stu, 'age'))
setattr(a_stu, 'age', 19)
print(hasattr(a_stu, 'age'), a_stu.age)
print(getattr(a_stu, 'score', -1))
# 可以获得对象的方法：
if hasattr(a_stu, 'score'):
    get_stu_score = getattr(a_stu, 'get_score')  # 先获取该名称的属性，没有这个属性，则取该名称的方法
    print(get_stu_score())
