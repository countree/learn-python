#!/usr/bin/python
# -*- coding: UTF-8 -*-
# encoding: utf-8
import os
import sys
from os.path import dirname

# should use: pip install delegator.py
import delegator
import pexpect

# 设置默认编码
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

child = ''


def connect(ip, name, pwd):
    global child
    cmd = "ssh {}@{}".format(name, ip)
    child = pexpect.spawn(cmd)
    child.expect('password:')
    print 'send-line:' + child.sendline(pwd)
    child.interact()


# 执行脚本
def exec_script():
    cmd = "sh docker-stats"
    body_ssh = pexpect.run(cmd)
    print 'from ssh body:%s' % body_ssh


if __name__ == '__main__':
    pexpect.run('ls')
    connect('192.168.2.188', 'root', 'root')
    exec_script()
