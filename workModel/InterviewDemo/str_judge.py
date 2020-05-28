
def bin_search(arr,target):
    first = 0
    last = len(arr) - 1

    while first <= last:

        mid = (first + last) // 2

        if arr[mid] > target:
            last = mid -1

        elif arr[mid] < target:
            first = mid + 1

        else:
            return True

    return False

if __name__ == '__main__':
    arr = [1,4,5,7,8]
    result = bin_search(arr, 5)
    print('二分查找法结果是：', result)
