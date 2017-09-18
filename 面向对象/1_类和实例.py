#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/17 17:38
# @Author  : zhangsheng

# 在Python中，定义类是通过class关键字：
# class后面紧接着是类名，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来.
# 如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。这和java一样的呀


class Student(object):
    # 通过定义__init__方法，把一些我们认为必须绑定的属性强制填写进去
    # __init__方法的第一个参数永远是self，表示创建的实例本身
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_stu_info(self):
        print('user info:%s: %s' % self.name, self.age)

    def get_stu_age(self):
        if self.age >= 18:
            print('老年人')
        else:
            print('小屁孩')


# 自由地给一个实例变量绑定属性
a_student = Student('zhangsheng', 18)
a_student.user_name = 'andy'

# 在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数
a_student.get_stu_age()

# Python允许对实例变量绑定任何数据，
# 也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
b_student = Student('dasheng', 12)
print(a_student.user_name)
# print(b_student.user_name)
