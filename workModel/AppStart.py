#1 /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import csv
import time

# 测试app冷启动和热启动时间
class AppStart(object):
    def __init__(self):
        self.content = ""
        self.start_time = 0

    def get_activity_name(self):
        adb_shell = os.popen('adb shell')
        get_activity_name = os.popen('adb shell logcat | grep START').split('=')
        for i, j in enumerate(get_activity_name):
            if 'cmp' == j:
                a = get_activity_name[i + 1]
                a.split(' ')
                b = a[0]
                print(b)

        print(get_activity_name)

    # 通过adb进入adb shel
    def adb_shell(self):
        cmd = ''


if __name__ == '__main__':
    AppStart()