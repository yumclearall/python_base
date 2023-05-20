import pandas as pd

# 导入matplotlib库的pyplot模块
from matplotlib import pyplot as plt
# 设置中文字体
plt.rcParams['font.family'] = ['Source Han Sans CN']

# 导入数据
my_data = pd.read_csv('工作/mask_data_clean.csv', encoding='utf-8')
# 查看my_data
my_data

# 获取行业的频率分布
profession = my_data['行业'].value_counts()/my_data['行业'].value_counts().sum()
# 绘制行业频率分布的饼图
profession.plot(kind='pie', autopct='%.2f%%', figsize=(7, 7), title='行业频率分布图', label='')

# 获取岗位的频率分布
position = my_data['岗位'].value_counts()/my_data['岗位'].value_counts().sum()
# 绘制岗位的频率分布条形图
position.plot(kind='bar', figsize=(13, 6), title='岗位频率分布条形图')

