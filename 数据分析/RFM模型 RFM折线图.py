import pandas as pd
import warnings

# 关闭警告显示
warnings.filterwarnings('ignore')

# 读取并查看【商品销售数据.xlsx】工作簿的数据
data = pd.read_excel('工作\工作\商品销售数据 rfm整理.xlsx')


import matplotlib.pyplot as plt

# 设置中文显示字体
plt.rcParams['font.family'] = ['SimHei']

# 画 R 值（时间间隔）的折线图，便于后续对数据进行分组
plt.figure(figsize=(10, 8))
x = data['时间间隔'].sort_values()
y = data.index
plt.plot(x, y)
plt.savefig('工作\工作\商品销售数据 R折线图.png')

# 画 F 值（总次数）的折线图，便于后续对数据进行分组
plt.figure(figsize=(10, 8))
x = data['总次数'].sort_values()
y = data.index
plt.plot(x, y)
plt.savefig('工作\工作\商品销售数据 S折线图.png')


# 画 M 值（总金额）的折线图，便于后续对数据进行分组
plt.figure(figsize=(10, 8))
x = data['总金额'].sort_values()
y = data.index
plt.plot(x, y)
plt.savefig('工作\工作\商品销售数据 M折线图.png')


