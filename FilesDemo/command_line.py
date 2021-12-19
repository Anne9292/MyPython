#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-20 09:29
# filename: PythonProjectDemo-command_line

import os


# 运行操作系统命令，控制台直接显示结果
def command_system(command):
    res = os.system(command)
    # return res.split('IPv4 Address. . . . . . . . . . . : ')
    print(res, type(res))


# 开启子进程执行命令，通过read()方法返回命令结果
def command_popen(command):
    res = os.popen(command)
    print(res.read())


if __name__ == '__main__':
    com = 'ipconfig'
    command_system(com)
