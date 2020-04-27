#!/usr/bin/python
# -*- coding: UTF-8 -*-
# encoding: utf-8
import logging
import sys

import schedule_send as sse

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

# 设置默认编码
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

if __name__ == '__main__':
    one_time = 's'
    if len(sys.argv) > 1:
        one_time = sys.argv[1]
    if one_time == 'one':
        sse.job()
    else:
        sse.start_job()
