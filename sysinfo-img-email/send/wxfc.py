#!/usr/bin/python
# coding=utf-8

import os
from os.path import dirname

from wxpy import *

# 设置默认编码
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

cachep = os.path.join(dirname(os.path.abspath(__file__)), 'wxlgcache.pk1')


def login():
    print '登录缓存key位置：' + cachep
    bot = Bot(console_qr=True, cache_path=cachep, qr_callback=qr(), login_callback=after_login(),
              logout_callback=logout())
    return bot


def qr():
    print '获取微信登录二维码后处理。。。'


def after_login():
    print '登录微信后处理。。。'


def logout():
    print '退出微信后处理。。。'
