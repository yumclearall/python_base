# 导入 pandas 模块并将其简化为 pd
import pandas as pd
# 导入pyplot模块
from matplotlib import pyplot as plt
# 设置显示中文字体
plt.rcParams['font.family'] = ['Source Han Sans CN']

# 生成画布，并设置画布的大小
plt.figure(figsize=(6, 6))
# 设置 x/y 坐标值
x = pd.Series(['第一季度', '第二季度', '第三季度', '第四季度'])
y = pd.Series([160, 200, 180, 155])
# 绘制折线图，并调整线条颜色为湖蓝色
plt.plot(x, y, color='dodgerblue')

# 生成画布，并设置画布的大小
plt.figure(figsize=(6, 6))
# 设置 x/y 坐标值
x = pd.Series(['第一季度', '第二季度', '第三季度', '第四季度'])
y = pd.Series([59, 70, 68, 56])
# 绘制柱状图，并调整颜色为深橘色，透明度为 60%
plt.bar(x, height=y, color='darkorange', alpha=0.6)
# 设置图表标题名为‘闪光科技2020年各季度研发费用分布图’及字体大小
plt.title('闪光科技2020年各季度研发费用分布图',fontsize=20)

# 设置坐标轴的刻度字体大小
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# 设置图表标题名及字体大小
plt.title('闪光科技2020年各季度研发费用分布图', fontdict={
        'family': 'Source Han Sans CN', 'color': 'blue', 'weight': 'bold', 'size': 16})

# 设置 x、y 轴标题分别为'季度'、'研发费用（百万元）'，字体大小均为 15
plt.xlabel('季度',fontsize=15)
plt.ylabel('研发费用（百万元）',fontsize=15)


# 生成画布，并设置画布的大小
plt.figure(figsize=(6, 6))
# 设置 x/y 坐标值
x = pd.Series(['第一季度', '第二季度', '第三季度', '第四季度'])
y = pd.Series([59, 70, 68, 56])
# 绘制折线图
plt.plot(x, y, color='dodgerblue')

# 绘制柱状图
plt.bar(x, height=y, color='darkorange', alpha=0.6)

# 设置图例为'研发费用变化'、'研发费用分布'
plt.legend(['研发费用变化','研发费用分布'])

# 生成画布，并设置画布的大小
plt.figure(figsize=(6, 6))
# 绘制柱状图
plt.bar(x, height=y, color='darkorange', alpha=0.6)

# 设置数据标签
plt.text('第一季度', 59, 59, ha='center', va='bottom', fontsize=12)
plt.text('第二季度', 70, 70, ha='center', va='bottom', fontsize=12)
plt.text('第三季度', 68, 68, ha='center', va='bottom', fontsize=12)
plt.text('第四季度', 56, 56, ha='center', va='bottom', fontsize=12)



x = pd.Series(['第一季度', '第二季度', '第三季度', '第四季度'])
y = pd.Series([59, 70, 68, 56])
for a, b in zip(x, y):
    print(a, b)

# 生成画布，并设置画布的大小
plt.figure(figsize=(6, 6))
# 绘制柱状图
plt.bar(x, height=y, color='darkorange', alpha=0.6)

# 设置数据标签
for x,y in zip(x,y):
    plt.text(x,y,y,ha='center',va='bottom',fontsize=12)