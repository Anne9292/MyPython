# -*- coding:utf-8 -*-

# # 列表
# list1 = ['Hello','World', 1, 2, 3]
# list2 = [3, 4, 5, 6]
# list3 = ['anne', 25, ['study', 'python']]
# print('list1[0]: ', list1[0])
# print('list2[:3]: ', list2[:-1])   # 切片
# print(list3[2][1])
# list2.append('anne')   # 更新列表，添加元素
# print(list2)
# del list1[4]
# print(list1)
# list1[2] = 'Test'
# print(list1)
#
# # 元组
# tup1 = "a", "b", "c"   #或者：tup1 = (1, 2, 'a')
# tup2 = ('a', 1, (2, 'b'))
# print(tup2[2][1])
# print(tup1)
# list1 = list(tup1)
# print(list1)
#
# # 集合
# producter = {'alex','humphy','harry','alex'}
# print(producter)   # 输出集合，重复元素自动去掉，无序
# # 成员测试
# if 'anne' in producter:
#     print('该成员在集合中')
# else:
#     print('该成员不在集合中')
# # set（）创建空集合，可以进行集合运算
# a = set('abcd')
# b = set('def')
# print(a)
# print(b)
# print(a - b)   # a和b的差集
# print(a | b)   # a和b的并集
# print(a & b)  # a和b的交集
# print(a ^ b)  # a和b中不同时存在的元素
#
# # 字典
# dict = {}
# dict['one'] = '1- 好好学习'
# dict[3] = '2- 天天向上'
# study = {'name': 'anne', 'age': 20, 'sex': 'female'}
# print(dict['one'])  # 输出键为‘one’的值
# print(dict[3])  # 输出键为3的值
# print(study)  # 输出完整字典
# print(study.keys())  # 输出字典所有键
# print(study.values())  # 输出字典所有至
# '''
# dict([('name','anne'),('age',2),('Taobao',4)])  # 构造函数dict()直接从键值对序列中构建字典
# {x: x**2 for x in {2, 4, 6}}
# dict(anne=4, age=20, sex='female')
# '''
#
# def a():
#     '''这是文档字符串'''
#     pass
# print(a.__doc__)
#
# for x in [1,2,3]: print(x, end=' ')

#去除首尾字符串
def trim(s):
    if len(s)==0:
        print(s)
    elif s[0]=='':
        print(s[1:len(s)])
    elif s[-1]=='':
        print(s[:len(s)-1])
    return s

def return_params(data):
    if data>=0:
        return data,data
    else:
        return data,-data


if __name__=='__main__':
    # if trim('') == '':
    #     print('1')
    # if trim(' hello ') == ' hello ':
    #     print("2")
    # if trim(' hello') == ' hello':
    #     print('3')
    orignal,result=return_params(-1)
    print(orignal, result)
    result=return_params(-1)
    print(result)