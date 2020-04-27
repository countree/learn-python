#!/usr/bin/python
# coding=utf-8

import os
from os.path import dirname

from PIL import Image, ImageDraw, ImageFont


def create_img(strs):
    img_path = os.path.join(dirname(os.path.abspath(__file__)), 'img', 'sysinfo.png')
    new_image(img_path, 600, 500, strs, show_image=True)
    return img_path


def draw_image(new_img, text, show_image=False):
    """
    画图
    :param new_img:
    :param text:
    :param show_image:
    :return:
    """
    try:
        text = text.decode('utf-8')
    except Exception, e:
        print e
    draw = ImageDraw.Draw(new_img)
    # img_size = new_img.size
    font_size = 12
    title_font_size = 9
    font_type = os.path.join(dirname(os.path.abspath(__file__)), 'font', 'consola.ttf')
    font_type_msyh = os.path.join(dirname(os.path.abspath(__file__)), 'font', 'msyhbd.ttc')
    text_lines = text.splitlines()
    x = 20
    y = 15
    for line in text_lines:
        print '>>>:' + line
        if line.strip() and is_chinese(line[0]):
            font_obj = ImageFont.truetype(font_type_msyh, title_font_size)
        else:
            font_obj = ImageFont.truetype(font_type, font_size)
        draw.text((x, y), line, font=font_obj, fill=(0, 0, 0))
        y += font_obj.getsize(line)[1] + 5
    if show_image:
        new_img.show()
    del draw


def is_chinese(word):
    word = word.encode('unicode-escape')
    if '\u4e00' <= word <= '\u9fff':
        return True
    return False


# 格式化字符串方法"r'%s_%s_%s.png' % (width, height, text)"

def new_image(filepath, width, height, text='default', color=(255, 255, 255, 255), show_image=False):
    """
    创建一个新的图片放在内存中

    :param filepath:
    :param width:
    :param height:
    :param text:
    :param color:
    :param show_image:
    :return:
    """
    new_img = Image.new('RGBA', (int(width), int(height)), color)
    # 画图片
    draw_image(new_img, text, show_image)
    # 保存内存中的图片到文件
    new_img.save(filepath)
    del new_img


if '__main__' == __name__:
    create_img(
        u"我去你大爷的，hello world 这么简单？？？\n\nhelloworld hahaha ddd \n eeee this file \n啊哈哈哈,我试试再说，得看会\nsee you memory")
