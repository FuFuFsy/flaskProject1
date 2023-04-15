'''
没用到的网页登录限制直接加到了app.py的代码里
'''
# -*- coding: utf-8 -*-
# 做登录限制，有些页面只有登录之后才能访问
# 通过定义装饰器实现
from functools import wraps
from flask import session, redirect, url_for


def login_required(func):
    @wraps(func)  # 防止传入的函数的一些签名丢失
    def wrapper(*args, **kwargs):
        if session.get("email"):
            # 当前处于登陆状态
            print(session.get('email'))
            return func(*args, **kwargs)
        else:
            return redirect(url_for("login"))

    return wrapper

