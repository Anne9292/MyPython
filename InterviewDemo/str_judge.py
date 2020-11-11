# -*- coding:utf-8 -*-

def str_judge(a):

    length = len(a)
    if length < 2 or length %2 != 0:
        if a == '':
            return True
        else:
            return False

    count = 1
    while count <= length/2:
        a = a.replace("{}","").replace("[]","").replace("()","")
        print('a是：',a)
        count += 1

    if len(a) > 0:
        return False
    else:
        return True

if __name__ == '__main__':
    a = input("请输入{/}/(/)/[/]此类字符串：")
    result = str_judge(a)
    print(result)

