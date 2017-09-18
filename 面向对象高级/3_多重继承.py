#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/18 16:44
# @Author  : zhangsheng

# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。


class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class RunnableMixIn(object):
    def run(self):
        print('Running...')


class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


# 各种动物:
class Dog(Mammal, RunnableMixIn):
    pass


class Bat(Mammal, FlyableMixIn):
    pass


a_dog = Dog()
a_dog.run()

# 不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类
