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
    │                                               │
    │   =============== 功能菜单 ===============     │
    │                                               │
    │   1 录入学生信息                                │
    │   2 查找学生信息                                │
    │   3 删除学生信息                                │ 
    │   4 修改学生信息                                │
    │   5 排序                                       │
    │   6 统计学生总人数                              │
    │   7 显示所有学生信息                            │
    │   0 退出系统                                   │
    │  ==========================================   │
    │  说明：通过数字或↑↓方向键选择菜单                 │
    ╚———————————————————————————————————————————————╝
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
    student_list = []
    mark = True
    while mark:
        while True:
            id = input("请输入ID（如1001）：")
            if id.isdigit():  # 判断字符串是否是整数
                break
            else:
                print("不能为空，只能输入数字")
        while True:
            name = input("请输入名字：")
            if name:
                break
            else:
                print("不能为空")
        try:
            english = input("请输入英语成绩：")
            python = input("请输入python成绩：")
            math = input("请输入数学成绩：")
        except BaseException:
            print("输入无效，不是整形数值......重新录入信息")
            continue
        student = {
            "id": id,
            "name": name,
            "english": english,
            "python": python,
            "math": math}
        student_list.append(student)
        input_mark = input("是否继续添加（y/n）：")
        if input_mark.strip(" ") == "y":
            mark = True
        else:
            mark = False
    save(student_list)
    print("学生信息录入完毕！！！")


def modify():
    pass


def delete():
    mark = True
    while mark:
        id = input("请输入要删除的学生ID：")
        if id is not "":
            if os.path.exists(filename):
                with open(filename, "r") as r_file:
                    student_old = r_file.readlines()
            else:
                student_old = []
            ifdel = False
            if student_old:
                with open(filename, "w") as w_file:
                    d = {}
                    for line in student_old:
                        d = dict(eval(line))
                        if d['id'] != id:
                            w_file.write(str(d) + '/n')
                        else:
                            ifdel = True
                    if ifdel:
                        print("ID为%s的学生信息已经被删除..." % id)
                    else:
                        print("没有找到ID为%s的学生信息..." % id)
            else:
                print("无学生信息...")
                break
            show()
            input_mark = input("是否继续删除？（y/n）：")
            if input_mark == "y":
                mark = True
            else:
                mark = False
        else:
            print("只能输入学生ID，不能为空")


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
        option_str = re.sub("\\D", "", option)  # 替换字符串中的非阿拉伯数字
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
