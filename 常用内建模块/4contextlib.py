#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 11:16
# @Author  : zhangsheng


# 实现上下文管理是通过__enter__和__exit__这两个方法实现的
from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen


class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


with Query('hello') as a_query:
    a_query.query()


# @contextmanager

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")

# closing


with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
