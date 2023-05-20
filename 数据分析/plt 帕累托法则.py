# 导入 pandas 库并将其简化为 pd
import pandas as pd
# 导入matplotlib库的pyplot模块
from matplotlib import pyplot as plt

# 读取练习数据，文件路径为 './工作/exercise_clean.csv'，文件编码为 'utf-8'
exercise = pd.read_csv('工作/mask_data_clean.csv', encoding = 'utf-8')
# 求出不同明细商品的总销工作\mask_data_clean.csv
sales_sum = exercise.groupby('明细')['订单金额'].sum()
# 设置中文字体
plt.rcParams['font.family'] = ['Source Han Sans CN']
# 生成画布，并设置画布的大小
plt.figure(figsize=(6, 6))
# 设置 x/y 坐标值
x = sales_sum.index
y = sales_sum.values
# 绘制柱状图，并调整柱子的样式
plt.bar(x, height=y, width=0.6, alpha=0.6)
# 设置图表标题名及字体大小
plt.title('各明细商品总销售额分布图', fontsize=20)
# 设置坐标轴的刻度字体大小，逆时针旋转x轴刻度90度
plt.xticks(fontsize=12, rotation=90)
plt.yticks(fontsize=12)
# 设置坐标轴的标题名及字体大小
plt.xlabel('商品明细', fontsize=15)
plt.ylabel('总销售额', fontsize=15)

# 求出累计销售额占比
p = 1.0*sales_sum.cumsum()/sales_sum.sum()

# 找到累计占比超过80%时候的index
key = p[p>0.8].index[0]  
key_num = sales_sum.index.tolist().index(key) 
print('超过80%累计占比的节点值索引为：' ,key)
print('------')

# 绘制折线图并将y轴设置为副坐标轴
p.plot(style = '--ko', secondary_y=True, rot=90)
plt.axvline(key_num,color='r',linestyle="--",alpha=0.8)
# 累计占比超过80%的节点
plt.text(key_num+0.2,p[key],'累计占比为：%.3f%%' % (p[key]*100), color = 'r')  

plt.ylabel('累计销售额占比')

plt.savefig('工作/帕累托法则图。png')