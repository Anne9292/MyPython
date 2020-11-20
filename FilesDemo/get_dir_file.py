# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : anne yang

import os

def get_dir_file(pathname):

    if not os.path.exists(pathname):
        print('sorry, have not this dir')
        os.mkdir(pathname)
    elif os.path.isdir(pathname):
        # 目录下既有文件又有文件夹
        for path, dirs, files in os.walk(pathname):
            print('\npath={},\ndirs={},\nfiles={}\n'.format(path, dirs, files))
            for name in dirs:
                print(os.path.join(path, name), '-------------遍历当前目录下的文件夹')
            for name in files:
                print(os.path.join(path, name), '-------------遍历当前目录下的文件')
        # 目录下只有文件，没有文件夹，可使用此方法
        # for filename in os.listdir(pathname):
        #     print(os.path.join(pathname, filename))

    elif os.path.isfile(pathname):
        # print(pathname.split('.')[-1])
        print(os.path.split(pathname))
        print(os.path.splitdrive(pathname))
        print(os.path.splitext(pathname))
        print(os.path.basename(pathname))
        print(os.path.abspath(pathname))

if __name__ == '__main__':
    get_dir_file(r'E:\test\test-1\test-2\冒烟测试不通过标准1.docx')
    # os.rmdir(r'E:\test\test-5')   # 删除空目录
    # os.rename(r'E:\test\test-1\test-3', r'E:\test\test-1\test-2')