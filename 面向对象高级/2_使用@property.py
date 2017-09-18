#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/18 16:00
# @Author  : zhangsheng


class Student(object):
    def __init__(self, score):
        self._score = score

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


# @property
# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值.
class People(object):
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


a_people = People(89)
a_people.score = 88  # 实际转化为s.set_score(88)
print(a_people.score)  # 实际转化为s.get_score()


# 可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

class Animal(object):
    def __init__(self, birth):
        self._birth = birth

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth


a_animal = Animal(2010)
# a_animal.birth = 2011
# a_animal.age = 12  # AttributeError: can't set attribute
print(a_animal.age)
