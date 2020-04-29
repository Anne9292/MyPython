#! /usr/bin/env python
# -*- coding:utf-8 -*-

# 打开D:\nyfedit7\myBase.ini文件,并删除某个字符串，用完会关闭文件
with open(r"D:\nyfedit7\myBase.ini","r") as f:
    lines = f.readlines()

with open(r"D:\nyfedit7\myBase.ini","w+",encoding="utf-8") as f:
    for line in lines:
        if "App.UserLic.FirstUseOn" in line:
            continue
        f.write(line)

# 查看该文件
f = open(r"D:/nyfedit7/myBase.ini","r",encoding="utf-8")
for line in f.readlines():
    print(line.strip())
f.close()