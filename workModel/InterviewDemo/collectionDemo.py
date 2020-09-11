# -*- coding：utf-8 -*-

from collections import Counter

str = ' aafagf;2qaad f '
res = Counter(str)
print(res)

res1 = dict(Counter(str).most_common())
print(res1)

print(len(str.lstrip()))   # 去掉左侧空格
print(len(str.rstrip()))	# 去掉右侧空格
print(str.strip())		# 去掉首尾空格
print(str.split(';'))		# 按照指定字符拆分成列表