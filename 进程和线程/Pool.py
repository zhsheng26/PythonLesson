#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/27 14:55
# @Author  : zhangsheng
import os
import random
import time
from multiprocessing import Pool


def task_pro(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    print('Task %s runs %0.2f seconds.' % (name, (time.time() - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    pool_task = Pool(4)  # 创建4个进程的进程池
    for i in range(5):  # 放5个任务进去
        pool_task.apply_async(task_pro, args=(i,))
    print('Waiting for all subprocesses done...')
    pool_task.close()
    pool_task.join()
    print('All subprocesses done.')
    # 对Pool对象调用join()
    # 方法会等待所有子进程执行完毕，调用join()
    # 之前必须先调用close()，调用close()
    # 之后就不能继续添加新的Process了
    # task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行
