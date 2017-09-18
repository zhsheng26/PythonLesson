#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/18 14:59
# @Author  : zhangsheng


# 在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
# 但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

class Student(object):
    stu_name = 'this is class attr'

    def __init__(self, stu_name):
        self.stu_name = stu_name


a_stu = Student('Andy')
print(a_stu.stu_name)
print(Student.stu_name)

del a_stu.stu_name
print(a_stu.stu_name)
########
a_stu.stu_name = 'Lily'
print(a_stu.stu_name)
