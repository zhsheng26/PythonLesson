#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/27 15:58
# @Author  : zhangsheng

# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据

from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码:
def write(qu):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        qu.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(qu):
    print('Process to read: %s' % os.getpid())
    while True:
        value = qu.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pr = Process(target=read, args=(q,))
    pw = Process(target=write, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
