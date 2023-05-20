import pandas as pd

# 导入matplotlib库的pyplot模块
from matplotlib import pyplot as plt
# 设置中文字体
plt.rcParams['font.family'] = ['Source Han Sans CN']

mask_data_clean = pd.read_csv('工作/mask_data_clean.csv',encoding='utf-8')
# 获取每月销售额总数
sales_income = mask_data_clean.groupby('月份')['销售额'].sum()
print(sales_income)

# 获取各月总订单量
order_number = mask_data_clean.groupby('月份')['订单量'].sum()
order_number

# 获取每月平均单价，存储在变量 month_price 中
month_price= mask_data_clean.groupby('月份')['单价'].mean()
month_price
# 查看数据

# 获取各月各省总订单量
month_order1=mask_data_clean.groupby(['月份','省'])['订单量'].sum()
# 查看数据
month_order1

# 画出各月总销售额的折线图
sales_income.plot(kind = 'line', figsize = (7, 7), title = '各月总销售额趋势图')

# 画出各月总订单量的折线图
order_number.plot(kind = 'line', figsize = (7, 7), title = '各月总订单量趋势图')

# 画出各月平均单价的折线图
month_price.plot(kind = 'line', figsize = (7, 7), title = '各月平均单价趋势图')

# 获取各月各省总订单量
month_order2 = mask_data_clean.groupby(['月份', '省'])['订单量'].sum()
# 查看数据
month_order2

# 将month_order1转换为DataFrame，存储在month_order1_df中
month_order1_df = month_order1.unstack()
# 查看month_order1_df中的数据
month_order1_df

# 根据month_order1_df绘制多条折线图，标题为'各月各省总订单量趋势图'
month_order1_df.plot(kind = 'line', figsize = (7, 7), title = '各月各省总订单量趋势图')

# 将month_order2转换为DataFrame，存储在month_order2_df中
month_order2_df = month_order2.unstack()
# 根据month_order2_df绘制多条折线图，标题为'各省各月总订单量趋势图'
month_order2_df.plot(kind = 'line',figsize = (7, 7), title = '各省各月总订单量趋势图')