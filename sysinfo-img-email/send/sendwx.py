#!/usr/bin/python
# coding=utf-8

from wxpy import *

import drawimg
import exec_shell as sysshell
import wxfc

logger = logging.getLogger(__name__)
# 设置默认编码
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)
bot = ''


def login():
    global bot
    if bot.alive:
        pass
    else:
        bot = wxfc.login()


def send(img_path):
    global bot
    try:
        if not bot.strip() or not bot.alive:
            login()
        oag_friend = ensure_one(bot.groups().search(u'2019研发'))
        oag_friend.send_image(img_path)
        # oag_friend.send_msg('测试')
        logger.info('消息发送完成')
    except ResponseError as e:
        logger.error('发送微信消息失败：%s,%s', str(e.err_code), e.err_msg)
        if e.err_code == 1100 or e.err_code == 1101 or e.err_code == 1102:
            logger.info('登录过期,请重新登录')
            try:
                bot = wxfc.login()
                send(img_path)
            except ResponseError as e1:
                logger.error('第二次登录微信并发送消息失败:%s' + e1.message)
        else:
            logger.error('发送微信消息失败，不是因为登录问题:%s', e.message)
            bot.logout


def job(body=''):
    if not body.strip():
        body = sysshell.getbody()
    img_path = drawimg.create_img(body)
    send(img_path)


def groups():
    global bot
    print bot.alive
    oag_friend = bot.groups()
    bot.logout()
    if not bot.alive:
        print '已经退出了', bot.alive
    print oag_friend


if __name__ == '__main__':
    login()
    groups()
    # job()
