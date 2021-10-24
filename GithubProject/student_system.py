#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: 豌豆
# datetime: 2021/10/6 21:37
# filename: MyPython/student_system

import os
import re

filename = os.path.join(os.path.dirname(__file__), "students.txt")

def menu():
    print('''
    ╔————————————————学生信息管理系统—————————————————╗
    │                                              │
    │   =============== 功能菜单 ===============     │
    │                                              │
    │   1 录入学生信息                               │
    │   2 查找学生信息                               │
    │   3 删除学生信息                               │
    │   4 修改学生信息                               │
    │   5 排序                                      │
    │   6 统计学生总人数                              │   
    │   7 显示所有学生信息                            │
    │   0 退出系统                                   │
    │  ==========================================  │
    │  说明：通过数字或↑↓方向键选择菜单                  │
    ╚——————————————————————————————————————————————╝
    ''')


def save(student):
    try:
        student_txt = open(filename, 'a')  # 追加模式打开
    except Exception as e:
        student_txt = open(filename, 'w')  # 文件不存在，创建新文件
    for info in student:
        student_txt.write(str(info) + '\n')
    student_txt.close()


def insert():
    pass


def modify():
    pass


def delete():
    pass


def search():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


def main():
    ctrl = True
    while ctrl:
        menu()
        option = input("请选择：")
        option_str = re.sub("\D", "", option)  # 替换字符串中的非阿拉伯数字
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0:
                print("您已退出学生信息管理系统！")
                ctrl = False
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()


if __name__ == '__main__':
    main()
