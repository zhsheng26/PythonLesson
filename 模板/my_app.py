#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/1 17:27
# @Author  : zhangsheng
from flask import Flask, render_template, request

hello = Flask(__name__)


@hello.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('home.html')


@hello.route('/singin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@hello.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('singin_ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


if __name__ == '__main__':
    hello.run()
