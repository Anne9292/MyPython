#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: 千泷（杨婷）
# @Email: qianlong.yang@tuya.com
# @Time: 2021/12/19 20:17
# @File: reader
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip)
from PyQt5.QtGui import QIcon, QFont


class FirstDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))  # 设置工具提示的字体
        self.setToolTip('This is a <b>anne first demo</b> QWidget widget')  # 创建提示，支持富文本格式
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')  # 创建PushButton，并设置tooltip
        btn.resize(btn.sizeHint())  # 显示默认尺寸
        btn.move(50, 50)
        self.setGeometry(300, 300, 300, 220)  # 设置窗口位置和大小
        self.setWindowTitle("FirstDemo")  # 设置窗口表态
        self.setWindowIcon(QIcon('headPicture.jpg'))  # 设置窗口图标
        self.show()  # 显示窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建应用程序和对象
    # w = QWidget()
    # w.resize(250, 150)
    # w.move(300, 300)
    # w.setWindowTitle("FirstDemo")
    # w.show()
    ex = FirstDemo()
    sys.exit(app.exec_())