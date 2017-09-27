#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/27 11:46
# @Author  : zhangsheng

# Unix/Linux操作系统提供了一个fork()系统调用

# 一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()  # fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
print('%s process running ' % pid)
if pid == 0:
    # 后走的这里，执行在子进程
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    # 先走的这里，返回子进程的pid,执行在父进程
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

