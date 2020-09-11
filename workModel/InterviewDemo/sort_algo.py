# -*- coding:utf-8 -*-

def bubble_sort(arr):
    '''比较相邻元素，若第1个比第2个大则交换，一轮交换完毕，最大数到最末尾，多次循环
    时间复杂度为O(n^2)'''

    for i in range(1, len(arr)):
        for n in range(len(arr)-i):
            if arr[n] > arr[n+1]:
                arr[n], arr[n+1] = arr[n+1], arr[n]
    print('冒泡排序结果是：', arr)


def selection_sort(arr):
    '''在未排序序列中找最小元素，放在排序序列起始位置；再从剩余未排序序列中找最小元素，放在已排序序列末尾
    时间复杂度为O(n^2)'''
    for i in range(len(arr)-1):
        minIndex = i  # 记录最小数的索引
        for j in range(i+1, len(arr)):   # 将未排序序列中的第一个值与其他值进行比较，找到最小值，并交换
            if arr[j] < arr[minIndex]:
                minIndex = j

        if i != minIndex:  # 未排序序列中找到的最小值比
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    print('选择排序结果是：', arr)


def insertion_sort(arr):
    '''将待排序序列第1个元素看做有序序列，将第2个元素到最后1个元素当成未排序序列，
    从头到尾扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
    时间复杂度为O(n^2)'''
    for i in range(1, len(arr)):
        value = arr[i]  # 待插入的数据
        j = i - 1   # 有序序列最后一位
        while j >= 0 and arr[j] > value:
            arr[j+1] = arr[j]   # 若有序序列元素比待插入元素大，将有序序列元素右移
            j -= 1
        arr[j+1] = value
    print('插入排序结果是：', arr)


def quick_sort(arr, left=None, right=None):
    '''1. 从数列中挑出一个元素，称为 "基准"（pivot）;
    2. 所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
    3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
    时间复杂度为O(nlogn)'''
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr)-1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quick_sort(arr, left, partitionIndex-1)
        quick_sort(arr, partitionIndex+1, right)
        print('快速排序结果是：', arr)

def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index-1)
    return index - 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    arr = [4, 3, 1, 5, 2, 6]
    # bubble_sort(arr) 
    # selection_sort(arr)
    # insertion_sort(arr)
    quick_sort(arr)



