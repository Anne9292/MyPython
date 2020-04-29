#! /usr/bin/env python
# _*_ coding:utf-8 _*_

# 从文件中读取图片，并写入到另一个文件中
fpath = r"C:\Users\anne\Documents\WeChat Files\TING215425\Files\1.txt"
# with open(fpath, 'r', encoding="utf-8") as f:
#     lines = f.readlines()
#
# with open(fpath,'a', encoding="utf-8") as f:
#     for line in lines:
#         if 'hello, world' in line:
#             continue
#         f.write(line)
try:
    sum = 1 + '1'
    with open(fpath) as f:
        print(f.read())

except OSError as reason:
    print('file has exception, the reason is: ' + str(reason))
except TypeError as reason:
    print(r"str and int type can't be use together~~~" + str(reason))
finally:
    print('Error ~~~~')