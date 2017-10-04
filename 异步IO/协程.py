#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/3 16:58
# @Author  : zhangsheng


# 一个generator
def consumer():
    r = ''
    while True:
        # 当produce调用send语句时，这里的yield仅用来接收参数交赋值给n， consumer不会产生中断
        # 当comsumer循环一圈后再执行到这里，此时produce还没有调用send，comsumer会中断执行
        n = yield r  # 拿到消息n，下面处理后再通过yield传回结果
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)  # 启动生成器，不会调用yield。参数不传None会报错，
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # 切换到consumer执行。拿到结果后继续
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()  # 关闭conumer


c = consumer()
produce(c)
