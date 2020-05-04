#1 /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import csv
import time

'''测试app冷启动和热启动时间'''
class App(object):

    def __init__(self):
        self.content = ""
        self.total_time = 0

    # 启动APP
    def launch_app(self):
        cmd = 'adb shell am start -W -n asia.bluepay.clientin/.business.module.login.FirstActivity'
        self.content = os.popen(cmd)  # 实时输出类文件对象，不会实时输出执行结果

    # 停止APP
    def stop_app(self):
        cmd = 'adb shell am force-stop asia.bluepay.clientin'  # 冷启动关闭app
        # cmd = 'adb shell input keyevent 3'  热启动关闭app
        os.popen(cmd)

    # 获取启动时间
    def get_launched_time(self):
        for line in self.content.readlines():
            if 'TotalTime' in line:
                self.total_time = line.split(': ')[1].split('\n')[0]
                break
        return self.total_time


# 控制类
class Controller(object):
    def __init__(self,count):
        self.app = App()
        self.counter = count
        self.all_data = [("timestamp","elapsed_time")]

    # 单次测试过程
    def test_process(self):
        self.app.launch_app()
        time.sleep(5)
        elapsed_time = self.app.get_launched_time()
        self.app.stop_app()
        time.sleep(3)
        current_time = self.get_current_time()
        self.all_data.append((current_time,elapsed_time))
        print(self.all_data)

    # 多次执行测试过程
    def run(self):
        while self.counter > 0:
            self.test_process()
            self.counter = self.counter - 1

    # 获取当前时间戳
    def get_current_time(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return current_time

    # 数据的存储
    def save_data_to_csv(self):
        csvfile = open('totalTime5.csv', 'w',newline='')
        writer = csv.writer(csvfile) # 创建初始化写入对象
        writer.writerows(self.all_data)  # 多行写入


if __name__ == '__main__':
    controller = Controller(5)
    controller.test_process()
    controller.save_data_to_csv()
