#!/usr/bin/python
# coding=utf-8
import logging
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import dirname

import email_config_parse as cfg

logger = logging.getLogger(__name__)

email_from = cfg.get_email('from')
email_password = cfg.get_email('password')
email_to_test = cfg.get_email('to')
email_to = cfg.get_email('topro')


def send_email_img(subject, body='', fp=''):
    send(subject, body, 'html', fp)


def send_email_txt(subject, body):
    send(subject, body, 'plain')


def send(subject, content, content_type, fp=''):
    """
    发送邮件及附件，附件目前只能是图片
    :param subject:
    :param content:
    :param content_type:
    :param fp: 附件文件路径
    :return:
    """
    mimeMult = MIMEMultipart()
    mimeMult['Subject'] = subject
    mimeMult['From'] = email_from
    mimeMult['To'] = email_to

    if fp.strip():
        content = '''<html lang="en">
    <body>
    <div>%s</div>
    <img src="cid:0">
    </body>
    </html>''' % content
    body = MIMEText(content, content_type, "utf-8")
    mimeMult.attach(body)

    if fp.strip():
        with open(fp, 'rb') as f:
            logger.info('附件地址:%s', fp)
            # 设置附件的MIME和文件名，这里是png类型:
            mime_file = MIMEBase('image', 'png', filename='systeminfo.png')
            # 加上必要的头信息:
            mime_file.add_header('Content-Disposition', 'attachment', filename='systeminfo.png')
            mime_file.add_header('Content-ID', '<0>')
            mime_file.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime_file.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime_file)
            # 添加到MIMEMultipart:
            mimeMult.attach(mime_file)

    try:
        s = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        s.login(email_from, email_password)
        s.sendmail(email_from, list(email_to.split(',')), mimeMult.as_string())
    finally:
        logger.info('发送邮件完成:' + subject)
        s.quit()


if __name__ == '__main__':
    email_to = email_to_test
    img_path = os.path.join(dirname(os.path.abspath(__file__)), 'img', 'sysinfo.png')
    send_email_img("测试附件", 'a', 'html', img_path)
