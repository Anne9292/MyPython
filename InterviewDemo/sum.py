def test_twoSum(nums, target):
    dct = {}
    for index, num in enumerate(nums):
        another_num = target - nums[index]
        if another_num in dct:  # 在dct字典中，another_num是key
            return [nums.index(another_num), index]
        else:
            dct[num] = index


if __name__ == '__main__':
    list1 = [2, 7, 11, 15]
    result = test_twoSum(list1, 17)
    print(result)
