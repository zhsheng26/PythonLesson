# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/24 16:33
# @Author  : zhangsheng


f = None
file_path = '/Users/zhangsheng/PycharmProjects/PythonLesson/文件读写/hello.txt'
try:
    f = open(file_path, 'r', encoding='utf-8')
    print(f.read())
finally:
    if f:
        f.close()

with open(file_path, 'r', encoding='utf-8') as f:
    print(f.read().strip())

    # 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
    # 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可

f = open(file_path, 'r', encoding='gbk', errors='ignore')
with f as file:
    print(f.read())

# 写文件

with open('/Users/zhangsheng/PycharmProjects/PythonLesson/文件读写/write.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, world!你好')
