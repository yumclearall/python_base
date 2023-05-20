# 请直接运行并体验代码

a = ''  # 设置一个字符串
print('字符串：')
print(dir(a))    # 把字符串相关的函数展示出来

a = []  # 设置一个列表
print('列表：')
print(dir(a))    # 把列表相关的函数展示出来

a = {}  # 设置一个字典
print('字典：')
print(dir(a))  # 把字典相关的函数展示出来

# 请直接运行并体验代码

import csv

# dir()函数会得到一个列表，用for循环一行行打印列表比较直观
for i in dir(csv):
    print(i)