# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : anne yang

import chardet
import os

def readFile(fpath):
    with open(fpath, 'r+', encoding='utf-8') as f:
        # print('一次读取整个内容：', f.read())
        # print('逐行读取', f.readline())
        f.write('\nyang')
        print('多行读取\n', f.readlines())

if __name__ == '__main__':
    fPath = r"data.txt"
    readFile(fPath)
