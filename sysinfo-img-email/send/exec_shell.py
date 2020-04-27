#!/usr/bin/python
# -*- coding: UTF-8 -*-
# encoding: utf-8
import os
import sys
from os.path import dirname

# should use: pip install delegator.py
import delegator

# 设置默认编码
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)


def getbody():
    body = exec_script()
    return body


# 执行脚本
def exec_script():
    usrhome = os.path.expanduser('~')
    scf = os.path.join(usrhome, 'docker-stats')
    sch = 'sh ' + scf
    if os.path.isfile(scf):
        c = delegator.run(sch)
    else:
        print '检测不到用户目录下执行文件：docker-stats,使用测试文件'
        pwd = dirname(os.path.abspath(__file__))
        sc = 'sh ' + os.path.join(pwd, 'shell', 'test-sysinfo.sh')
        c = delegator.run(sc)

    # print '脚本执行完结果：\n' + c.out
    return c.out


if __name__ == '__main__':
    print 'body:\n' + getbody().replace(' ', '-')
