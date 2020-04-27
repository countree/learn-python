#!/usr/bin/python
# -*- coding: UTF-8 -*-
# encoding: utf-8
import logging
import socket
import sys
import time

# should use: pip install delegator.py
import schedule

import drawimg
import email_config_parse as cfg
import exec_shell as execshell
import qqmail
import sendwx

# 设置默认编码
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

logger = logging.getLogger(__name__)

# msg_to = "hanbing.yangyanhui@xiaojiantech.com"

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
subject = "服务系统运行情况检测:" + ip + "-" + hostname


def job():
    print "开始执行任务"
    logger.info("开始执行任务")
    body = getbody()
    img_path = drawimg.create_img(subject + '\r\n' + body)
    qqmail.send_email_img(subject, '', img_path)
    # try:
    #     sendwx.send(img_path)
    # except BaseException as e:
    #     logger.error('执行发送微信错误:%s', e.message)


def getbody():
    body = execshell.getbody()
    return body


def start_job():
    print "开始启动定时任务,获取系统信息。将会在每天 " + cfg.get_schedule('send_time') + " 发送邮件"
    schedule.every().day.at(cfg.get_schedule('send_time')).do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


# =======test===========

if __name__ == '__main__':
    job()
