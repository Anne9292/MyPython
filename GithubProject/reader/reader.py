# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reader.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        # 设置主窗口大小
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.centralwidget.setObjectName("centralwidget")
        # 设置抓取设置窗口位置大小
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 511, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        # 设置抓取期数labal
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # 设置保存路径label
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        # 设置期数范围label
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(330, 30, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        # 设置抓取期数文本框
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 30, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        # 设置保存路径文本框
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(160, 70, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        # 设置选择按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 70, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setObjectName("pushButton_2")
        # 设置确定按钮
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(200, 110, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setObjectName("pushButton")
        # 设置文件预览窗口位置大小
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 170, 511, 341))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        # 设置选项卡窗口
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget.setGeometry(QtCore.QRect(0, 30, 511, 341))
        self.tabWidget.setObjectName("tabWidget")
        # 设置按日期显示tab
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        # 设置按日期显示表格窗口
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 511, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(0, 130)  # 设置第一列宽度
        # 设置自动填充容器
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # 显示垂直滚动条
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabWidget.addTab(self.tab, "")
        # 设置按名称显示tab
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        # 设置按名称显示列表窗口
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 511, 321))
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab_2, "")
        self.listWidget.setIconSize(QtCore.QSize(72, 72))  # 图标大小
        self.listWidget.setMaximumWidth(800)  # 最大宽度
        self.listWidget.setSpacing(12)  # 间距大小
        # 显示垂直滚动条
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """用来设置窗体中控件的默认值"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "安妮的小书屋"))
        self.groupBox.setTitle(_translate("MainWindow", "抓取设置"))
        self.label.setText(_translate("MainWindow", "请选择抓取期数："))
        self.label_2.setText(_translate("MainWindow", "请选择保存路径："))
        self.label_3.setText(_translate("MainWindow", "（期数范围为01——24）"))
        self.pushButton_2.setText(_translate("MainWindow", "选择"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.groupBox_2.setTitle(_translate("MainWindow", "文件预览"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(
                self.tab), _translate(
                "MainWindow", "按日期显示"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(
                self.tab_2), _translate(
                "MainWindow", "按名称显示"))
        strDate = str(time.localtime().tm_year) + '-' + str(time.localtime().tm_mon)
        self.lineEdit_2.setText(_translate("MainWindow", strDate))
        self.lineEdit.setText(_translate("MainWindow", os.getcwd()))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "期数"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "名称"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = QtWidgets.QMainWindow()  # 创建窗体对象
    ui = Ui_MainWindow()  # 创建pyqt5的创建对象
    ui.setupUi(mw)  # 调用pyqt5窗体的方法对窗体对象进行初始化设置
    mw.show()  # 显示窗体
    sys.exit(app.exec_())
