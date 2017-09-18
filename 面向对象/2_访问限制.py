#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/17 17:55
# @Author  : zhangsheng


# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_stu(self):
        print(self.__name, self.__score)

    def get_name(self):
        return self.__name


a_stu = Student('andy', 19)
a_stu.print_stu()
# a_stu.__name  AttributeError: 'Student' object has no attribute '__name'

# Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
print(a_stu._Student__name)

# 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
# 一个下划线开头的实例变量名:虽然我可以被访问，但是，请把我视为私有变量，不要随意访问


a_stu.__name = "zhangsheng"  # 实际上这个__name变量和class内部的__name变量不是一个变量.这里是新增了一个变量！
print(a_stu.get_name())
