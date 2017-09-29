#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/27 21:07
# @Author  : zhangsheng
from datetime import datetime

# 获取当前日期和时间
print(datetime.now())
# 获取指定日期和时间
print(datetime(2017, 9, 27, 12, 20))
# 时间戳 :如果有小数位，小数位表示毫秒数。
print(datetime.timestamp(datetime(2017, 9, 27, 12, 20)))

# str转换为datetime

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
print(type(cday))
# datetime转str
print(datetime.now().strftime('%a, %b %d %H:%M'))
