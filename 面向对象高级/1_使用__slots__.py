#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/18 15:19
# @Author  : zhangsheng

# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法
from types import MethodType


class Student(object):
    pass


a_stu = Student()
# 给实例绑定属性
a_stu.user_name = 'andy'


# 给实例绑定方法
def set_age(self, age):
    self.age = age


a_stu.set_age = MethodType(set_age, a_stu)
a_stu.set_age(100)
print(a_stu.age)

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
b_stu = Student()
# print(b_stu.age)  # 'Student' object has no attribute 'age'


# 给class绑定方法：
Student.set_age = set_age
b_stu.set_age(88)
print(b_stu.age)


# 动态绑定允许我们在程序运行的过程中动态给class加上功能


# ######### 使用__slots__限制实例的属性  ##########
class People(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


a_people = People()
a_people.name = 'china'
# a_people.address = 'hefei'

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
