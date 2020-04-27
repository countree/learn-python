#!/usr/bin/python
# coding=utf-8

import os
import time
from os.path import dirname

import schedule
from wxpy import *

import wxfc

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

# 设置默认编码
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

    # 向文件传输助手发送消息
    # bot.file_helper.send('Hello from wxpy!')
bot = wxfc.login()


def send():
    global bot
    try:
        qinqin_friend = ensure_one(bot.friends().search(u'亲亲'))
        img_path = os.path.join(dirname(os.path.abspath(__file__)), 'sb.png')
        print '图片路径：' + img_path
        qinqin_friend.send_image(img_path)
        logger.info('消息发送完成')
        print '消息发送完成：'
    except ResponseError as e:
        print(e.err_code, e.err_msg)
        if e.err_code == 1100 or e.err_code == 1101 or e.err_code == 1102:
            logger.info('登录过期,请重新登录')
            print '登录过期,请重新登录'
            # bot = wxfc.login()
            # send()
        else:
            print '发送微信消息失败'


def start_job():
    schedule.every().day.at('08:10').do(send)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    start_job()
    logger.info('执行main完成')
    print '执行main完成'
