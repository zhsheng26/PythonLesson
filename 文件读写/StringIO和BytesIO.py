#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/24 17:43
# @Author  : zhangsheng

from io import StringIO

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
str_io = StringIO()
str_io.write('hello')
str_io.write(' ')
str_io.write('python')
print(str_io.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')

while True:
    line = f.readline()
    if line == '':
        break
    print(line.strip())

    # 操作二进制数据，就需要使用BytesIO。

from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())  # b'\xe4\xb8\xad\xe6\x96\x87'
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
