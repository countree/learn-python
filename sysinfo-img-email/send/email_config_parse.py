#!/usr/bin/python
# coding=utf-8
import ConfigParser
import os
from os.path import dirname

'解析email配置文件'

# 下面这种方式获取的路径不靠谱，如果执行脚本的目录不是这个目录就报错了
# 获取当前脚本执行时的路径
cwdir = os.getcwd()
# 通过相对此文件位置获取靠谱
pwdir = dirname(os.path.abspath(__file__))
print '当前文件夹路径>' + pwdir
print '父文件夹路径>' + dirname(pwdir)
config_filename = os.path.join(dirname(pwdir), 'config', 'email.ini')

with open(config_filename, 'r') as fr:
    cfg = ConfigParser.ConfigParser()
    cfg.readfp(fr)
    print '所有section:' + ','.join(cfg.sections())


def get_email(key):
    return cfg.get('email', key)


def get_schedule(key):
    return cfg.get('schedule', key)
