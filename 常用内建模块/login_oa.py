#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 15:19
# @Author  : zhangsheng
import calendar
import json
from datetime import datetime
from threading import Timer

import requests

print('Login to TimeFace oa...')

base_url = 'http://oa.v5time.net/tfoa/'

session = requests.Session()
headers = {'Host': 'oa.v5time.net',
           'Origin': 'http://oa.v5time.net',
           'Accept': 'application/json, text/plain, */*',
           'Accept-Encoding': 'gzip, deflate',
           'Referer': 'http://oa.v5time.net/tfoa/index/frontpage',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38'}

MORNING = 'morning'
NOON = 'noon'
EVENING = 'evening'

USER_NAME = 'zhangsheng@timeface.cn'


def login_user():
    login_url = base_url + 'auth/login'
    login_param = {'email': USER_NAME, 'password': 'MTExMTEx'}
    r = session.get(login_url, params=login_param)
    return r.status_code == 200


def query_check_state(key):
    attendance_state_url = base_url + 'onlineAttendance/current'
    attendance = session.post(attendance_state_url, headers=headers)
    if attendance.status_code == 200:
        json_attendance = json.loads(attendance.text)
        return json_attendance[key]
    else:
        return ''


def get_token():
    token_url = "http://tat.tfdom.com/api/v1/token"
    token_req = requests.get(token_url, params={'email': USER_NAME})
    return json.loads(token_req.text)['token']


def cache_token(now_token):
    cache_url = base_url + 'onlineAttendance/cache'
    cache_resp = session.post(cache_url, data={'token': now_token}, headers=headers)
    print(cache_resp.text)


def sign(key):
    if not login_user():
        return
    sign_time = query_check_state(key)
    if sign_time:
        print(key + ' 已打卡，打卡时间：%s' % sign_time)
    else:
        # 未打开，可以打卡了
        token = get_token()
        cache_token(token)
        sign_url = base_url + 'onlineAttendance/sign'
        if key == MORNING:
            flag = 1
        elif key == NOON:
            flag = 2
        else:
            flag = 3
        sign_res = session.post(sign_url, data={'flag': flag}, headers=headers)
        print(sign_res.text)


def get_should_sign_time(hour, minute):
    return datetime(datetime.today().year, datetime.today().month, datetime.today().day, hour, minute).strftime(
        '%Y-%m-%d %H')


# 登录
# 检查打卡状态
# 获取当前时间，判断是否是需要打卡的时间
# 打卡
# sign(MORNING)
def start_sign():
    # 星期天不打卡
    if datetime.today().weekday() == calendar.SUNDAY:
        return
    elif datetime.today().weekday() == calendar.SATURDAY:
        # 8:30
        time = datetime.today().time()
        print(time)
        # 12:30
        return
    else:
        current_time = datetime.today().__format__('%Y-%m-%d %H')
        sign_morning = get_should_sign_time(8, 0)  # 早上
        sign_noon = get_should_sign_time(13, 0)  # 中午
        sign_evening = get_should_sign_time(18, 0)  # 晚上
        print('current_time = %s ;sign_morning = %s ;sign_noon = %s ;sign_evening = %s'
              % (current_time, sign_morning, sign_noon, sign_evening))
        if current_time == sign_morning:
            sign(MORNING)
        elif current_time == sign_noon:
            sign(NOON)
        elif current_time == sign_evening:
            sign(EVENING)
        else:
            print('还没到打卡时间呢。。。')
    run_sign()


def run_sign():
    Timer(1 * 60 * 10, start_sign).start()


if __name__ == '__main__':
    start_sign()
