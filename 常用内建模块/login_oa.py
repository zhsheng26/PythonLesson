#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 15:19
# @Author  : zhangsheng
import calendar
import json
from datetime import datetime
from threading import Timer

import requests

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

print(USER_NAME + ' \nLogin to TimeFace oa...')


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


def cache_token():
    token_url = "http://tat.tfdom.com/api/v1/token"
    token_req = requests.get(token_url, params={'email': USER_NAME})
    now_token = json.loads(token_req.text)['token']
    cache_url = base_url + 'onlineAttendance/cache'
    cache_resp = session.post(cache_url, data={'token': now_token}, headers=headers)
    print(cache_resp.text)


def sign(key):
    sign_time = query_check_state(key)
    if sign_time:
        print(key + ' 已打卡，打卡时间：%s' % sign_time)
    else:
        cache_token()
        sign_url = base_url + 'onlineAttendance/sign'
        if key == MORNING:
            flag = 1
        elif key == NOON:
            flag = 2
        else:
            flag = 3
        sign_res = session.post(sign_url, data={'flag': flag}, headers=headers)
        if sign_res.status_code == 200:
            print('==*=====%s======*==' % sign_res.text)
            query()


def get_should_sign_time(hour, minute):
    return datetime(datetime.today().year, datetime.today().month, datetime.today().day, hour, minute).strftime(
        '%Y-%m-%d %H:%M')


# 登录
# 检查打卡状态
# 获取当前时间，判断是否是需要打卡的时间
# 打卡

def start_sign():
    morning_h = 8
    morning_m = 20

    noon_h = 12
    noon_m = 7

    evening_h = 18
    evening_m = 8
    # 星期天不打卡
    weekday = datetime.today().weekday()
    if weekday == calendar.SUNDAY:
        return
    else:
        current_time = datetime.today().__format__('%Y-%m-%d %H:%M')
        sign_morning = get_should_sign_time(morning_h, morning_m)  # 早上
        sign_noon = get_should_sign_time(noon_h, noon_m)  # 中午
        if weekday == calendar.TUESDAY or weekday == calendar.THURSDAY:
            evening_h = 21
            evening_m = 4
        sign_evening = get_should_sign_time(evening_h, evening_m)  # 晚上
        if current_time == sign_morning:
            sign(MORNING)
        elif current_time == sign_noon:
            sign(NOON)
        elif current_time == sign_evening:
            sign(EVENING)
    run_sign()


def run_sign():
    Timer(1 * 10, start_sign).start()


def query():
    state_morning = query_check_state(MORNING)
    if state_morning:
        print('早上已打卡：%s' % state_morning)
    else:
        print('早上待打卡...')
        return
    state_noon = query_check_state(NOON)
    if state_noon:
        print('中午已打卡：%s' % state_noon)
    else:
        print('中午待打卡...')
        return
    state_evening = query_check_state(EVENING)
    if state_evening:
        print('晚上已打卡：%s' % state_evening)
    else:
        print('晚上待打卡...')
        return


if __name__ == '__main__':
    if login_user():
        print('登录成功!')
        query()
        start_sign()
