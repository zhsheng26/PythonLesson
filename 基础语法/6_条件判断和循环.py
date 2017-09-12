#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/12 11:22
# @Author  : zhangsheng

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

all_sum = 0
for i in range(101):
    all_sum += i
print(all_sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello %s' % name)

# break语句可以提前退出循环
# continue语句，跳过当前的这次循环，直接开始下一次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
