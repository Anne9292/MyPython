# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : anne yang

import os

def get_dir_file(pathname):
    for path, dirs, files in os.walk(pathname, topdown=False):
        for name in files:
            print(os.path.join(path, name), '当前目录下的文件遍历')
        for name in dirs:
            print(os.path.join(path, name), '当前文件夹下的目录遍历')

if __name__ == '__main__':
    get_dir_file('./')