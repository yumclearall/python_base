import pandas as pd
import warnings

# 关闭警告显示
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt


# 读取并查看【商品销售数据.xlsx】工作簿的数据
rfm_data = pd.read_excel('工作\工作\商品销售数据 rfm整理3.0.xlsx')

# 按【客户类型】分组，统计用户的数量
customer_data =rfm_data.groupby('客户类型')['用户 ID'].count()
customer_data

# 设置中文字体
plt.rcParams['font.family'] = ['SimHei']

# 绘制柱状图
plt.figure(figsize=(12, 8))
plt.bar(customer_data.index, customer_data)
plt.xlabel('客户类型', fontsize=12)
plt.ylabel('人数', fontsize=12)
plt.title('不同客户的数量分布', fontsize=16)
plt.savefig('工作\工作\商品销售数据 RFM条形图.png')

# 绘制饼图
plt.figure(figsize=(14, 10))
plt.pie(customer_data, labels=customer_data.index, autopct='%0.1f%%')
plt.title('不同客户占比情况', fontsize=16)
plt.savefig('工作\工作\商品销售数据 RFM饼图.png')
