#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2021-03-03 19:25
# filename: MyPython/bubble_sort

# 原始冒泡排序方法
def bubble_0(arr):
    length = len(arr)
    count = 0
    for i in range(length-1):
        for j in range(length-i-1):
            count += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(f'bubble_0执行{count}次')
    return arr

# 改进版冒泡排序
def bubble_1(arr):
    length = len(arr)
    count = 0
    for i in range(1, length):
        swap_flag = False  # 判断是否交换的标志位
        for j in range(length - i):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_flag = True
        if not swap_flag:
            break
    print(f'bubble_1执行{count}次')
    return arr

if __name__ == '__main__':
    arr_0 = [1, 2, 3, 4, 5]
    arr_1 = [5, 4, 3, 2, 1]
    arr_2 = [1, 3, 2, 5, 4]
    # res_0 = bubble_0(arr_1)
    res_1 = bubble_1(arr_2)
    print(res_1)