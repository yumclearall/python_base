# 导入 pandas 模块并将其简化为 pd
import pandas as pd
# 导入pyplot模块
from matplotlib import pyplot as plt
# 设置显示中文字体
plt.rcParams['font.family'] = ['SimHei']
#
mask_data_clean= pd.read_csv('工作/mask_data_clean.csv',encoding='utf-8')
# 求得各月平均单价数据，并将其赋值给变量 mask_price
mask_price = mask_data_clean.groupby('月份')['单价'].mean()
# 查看mask_price
mask_price
# 生成画布，并设置画布的大小为(6, 6)
plt.figure(figsize=(6,6))
# 设置 x 坐标值为月份信息，y 坐标值为各月口罩平均单价
x=mask_price.index
y=mask_price.values
# 绘制柱状图，调整柱子的样式，并区分 1 月份和 6 月份颜色
plt.bar(x,height=y,color=['r','g','b','m','c','y'],width=0.6,alpha=0.6)
# 设置图表标题名为'各月平均单价分布图'，字体大小为 20
plt.title('各月平均单价分布图',fontsize=20)
# 坐标轴的刻度字体大小为 12
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# 设置 x、y 轴标题分别为'月份'、'各月平均单价（元）'，字体大小均为 15
plt.xlabel('月份',fontsize=15)
plt.ylabel('各月平均单价（元）',fontsize=15)
# 为柱子添加每一个数据标签，数值是 y 坐标值，并且只保留整数
for x,y in zip(x,y):
    plt.text(x,y,y,ha='center',va='bottom',fontsize=10)
# 设置画布保存路径为'./工作/各月平均单价分布图.png'
plt.savefig('工作/各月平均单价分布图.png')

# 生成各类明细商品的总销售额的折线图，将 x 轴的刻度逆时针旋转 90 度
#sales_sum.plot(rot=90)   rotation
# 降序排列sales_sum
#sales_sum = sales_sum.sort_values(ascending=False)
# 查看sales_sum
#sales_sum