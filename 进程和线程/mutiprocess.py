#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/27 14:48
# @Author  : zhangsheng

# multiprocessing
import os
from multiprocessing import Process


def run_task(name):
    print('子进程:%s 执行任务:%s' % (os.getpid(), name))


if __name__ == '__main__':
    print('parent process: %s' % os.getpid())
    down_process = Process(target=run_task, args=('下载...',))
    down_process.start()
    down_process.join()  # 如果不写，后面的可能会在子任务执行之前执行
    # join()方法，等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('process finish %s' % os.getpid())
