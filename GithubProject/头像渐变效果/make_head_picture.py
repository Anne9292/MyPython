#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: 豌豆
# datetime: 2021/10/24 15:36
# filename: MyPython/make_head_picture

import os
from PIL import Image


def make_head_picture(bg_im, head_im, im):
    bg_pic = Image.open(bg_im).convert('RGBA')
    head_pic = Image.open(head_im).convert('RGBA')
    x, y = bg_pic.size  # 获取背景图片的尺寸
    # 元组里的元素分别是：距离左边界距离=左上角x, 距离上边界距离=左上角y，宽度，高度
    area = bg_pic.crop((0, 0, x, y))
    w, h = head_pic.size  # 获取头像的尺寸
    area = area.resize((w, h))
    for i in range(w):  # 透明度渐变设置
        for j in range(h):
            # 获取像素点的颜色值，返回元组（R,G,B,alpha），RGB值和透明度，255不透明，0是100%透明
            color = area.getpixel((i, j))
            alpha = 255 - i // 2
            if alpha < 0:
                alpha = 0
            color = color[:-1] + (alpha,)
            area.putpixel((i, j), color)  # 对像素点设置颜色
    head_pic.paste(area, mask=area)
    head_pic.save(im)


if __name__ == '__main__':
    bg = 'guoqi.jpg'
    head = '镜玄.jpeg'
    after = '国庆渐变头像.png'
    make_head_picture(bg, head, after)
