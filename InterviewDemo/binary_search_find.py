#! -*- coding:utf-8 -*-

def binary_search_func(list, key):

    first = 0
    last = len(list) - 1

    while first <= last:
        mid = (first + last) // 2
        if arr[mid] < key:
            first = mid + 1
        elif arr[mid] > key:
            last = mid - 1
        else:
            return mid
    return False

if __name__ == '__main__':
    arr = [3,2,1,5,4]
    result = binary_search_func(arr, 4)
    print('list key is:', result)
