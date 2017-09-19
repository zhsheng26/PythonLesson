#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/18 17:10
# @Author  : zhangsheng


# 形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的


# 特殊用途的函数
# ###########  __slots__      ###########
# ###########  __len__()      ###########
# ###########  __str__()      ###########
# ###########  __iter__()     ###########
# ###########  __getitem__()  ###########
# ###########  __getattr__()  ###########
# ###########  __call__()     ###########


# ###########  __str__()      ###########
class Student(object):
    def __init__(self, stu_name):
        self._name = stu_name

    @property
    def stu_name(self):
        return self._name

    @stu_name.setter
    def stu_name(self, name):
        self._name = name

    def __str__(self):
        return 'Student object (name: %s)' % self._name

    __repr__ = __str__


a_student = Student('andy')
print(a_student)


# __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串


# ###########  __iter__()     ###########

# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。


# ###########  __getitem__()  ###########
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：


# ###########  __getattr__()  ###########

class Employee(object):
    def __init__(self):
        self.name = 'Michael'

    # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        elif attr == 'age':
            return lambda: 25
        # 不加下面的异常处理，会返回None，这是因为我们定义的__getattr__默认返回就是None
        else:
            raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


a_employee = Employee()
print(a_employee.name)
print(a_employee.score)
print(a_employee.age())


# print(a_employee.aaaaa)  # 会返回None，这是因为我们定义的__getattr__默认返回就是None

# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

# 利用完全动态的__getattr__，我们可以写出一个链式调用：

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print('=======')
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, attr):
        return Chain('%s/%s' % (self._path, attr))

    __repr__ = __str__


# print(Chain().status.user.timeline.list)  # /status/user/timeline/list
print(Chain().users('michael').repos)  # /users/:user/repos

# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
# 我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
print(callable(max))
print(callable('str'))
