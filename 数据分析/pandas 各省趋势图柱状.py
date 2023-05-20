# 导入 pandas 模块并将其简化为 pd
import pandas as pd
# 导入pyplot模块
from matplotlib import pyplot as plt
# 设置显示中文字体
plt.rcParams['font.family'] = ['SimHei']
#
mask_data_clean= pd.read_csv('工作/mask_data_clean.csv',encoding='utf-8')
# 提取各省各月订单量数据
month_order = mask_data_clean.groupby(['月份', '省'])['订单量'].sum()
# 将多级索引的的Series对象转换成DataFrame对象
month_order_df = month_order.unstack()
# 查看各省各月订单量数据
month_order_df
# 生成画布，并设置画布的大小为(6, 6)
plt.figure(figsize=(6,6))
# 设置 x 坐标值为月份信息，y 坐标值为各个省份在各月口罩订单总量的信息
x=month_order_df.index
y=month_order_df.values
# 绘制折线图，并调整线条、标记点的样式
plt.plot(x,y,linewidth=3,marker='o',markerfacecolor='w',markersize=10)
# 设置图表标题名为'各省各月口罩订单量变化折线图'，字体大小为 20
plt.title('各省各月口罩订单量变化折线图',fontsize=20)
# 设置坐标轴的刻度字体大小为 12
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# 设置 x、y 轴标题分别为'月份'、'各省各月口罩订单量（百万）'，字体大小均为 15
plt.xlabel('月份',fontsize=15)
plt.ylabel('各省各月口罩订单量（百万）',fontsize=15)
# 添加图例，内容为：'其他', '广东', '江苏', '河南', '湖北', '湖南'
plt.legend(['其他', '广东', '江苏', '河南', '湖北', '湖南'])
# 设置画布保存路径为'./工作/各省各月口罩订单量变化折线图.png'
plt.savefig('工作/各省各月口罩订单量变化折线图3.png')




