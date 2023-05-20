# 导入 pandas 模块并将其简化为 pd
import pandas as pd
# 导入pyplot模块
from matplotlib import pyplot as plt
# 设置显示中文字体
plt.rcParams['font.family'] = ['Source Han Sans CN']
# 读取清洗好的数据'./工作/mask_data_clean.csv'，并赋值给 mask_data_clean 变量
mask_data_clean =pd.read_csv('工作/mask_data_clean.csv',encoding='utf-8')
# 查看 mask_data_clean
mask_data_clean

# 获取各月总订单量的数据
order_number = mask_data_clean.groupby('月份')['订单量'].sum()
# 绘制各月订单总量的折线图
order_number.plot(kind='line', figsize=(6, 6), title='各月总订单量趋势图')

# 生成画布，并设置画布的大小
plt.figure(figsize=(6, 6))

# 绘制图表
x = order_number.index
y = order_number.values
plt.plot(x, y)

# 保存画布，并设置保存路径
plt.savefig('工作/各月总订单量趋势图.png')

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