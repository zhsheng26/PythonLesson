#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/18 10:38
# @Author  : zhangsheng

# 和java基本一样

# 定义一个父类类型的引用指向一个子类的对象既可以使用子类强大的功能，又可以抽取父类的共性。
# 所以，父类类型的引用可以调用父类中定义的所有属性和方法，而对于子类中定义而父类中没有的方法，它是无可奈何的；
# 同时，父类中的一个方法只有在在父类中定义而在子类中没有重写的情况下，才可以被父类类型的引用调用；
# 对于父类中定义的方法，如果子类中重写了该方法，那么父类类型的引用将会调用子类中的这个方法，这就是动态连接。

###############################
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
###############################
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
###############################


class Animal(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name + " run...")


class Dog(Animal):
    pass


a_dog = Dog('hali')
a_dog.run()


class People(object):
    @staticmethod
    def run():
        print('this is man run')


# 我们只需要保证传入的对象有一个run()方法就可以了
def let_go(runObj):
    runObj.run()


a_people = People()
let_go(a_dog)
let_go(a_people)
