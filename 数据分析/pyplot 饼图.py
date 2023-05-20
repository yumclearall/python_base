# 导入 pandas 模块并将其简化为 pd
import pandas as pd
# 导入pyplot模块
from matplotlib import pyplot as plt
# 设置显示中文字体
plt.rcParams['font.family'] = ['SimHei']

# 生成画布，并设置画布的大小
plt.figure(figsize=(6, 6))
# 设置扇形面积值
x = pd.Series([59, 70, 68, 56])
# 设置百分比小数的位数：保留百分比小数点后两位
autopct='%.2f%%'
# 设置百分比字体大小和颜色
textprops = {'fontsize': 12, 'color': 'black'}
# 设置饼图的“爆炸效果”：让扇形远离圆心
explode = [0.1, 0, 0, 0]
# 设置不同扇形的颜色
colors = ['cornflowerblue', 'salmon', 'yellowgreen', 'orange']
# 绘制饼图
plt.pie(x, autopct=autopct, textprops=textprops,
        explode=explode, colors=colors)
# 设置图表标题名及字体大小
plt.title('闪光科技2020年各季度研发费用占比饼图', fontsize=20)
# 设置图例
plt.legend(['第一季度', '第二季度', '第三季度', '第四季度']) 

plt.savefig('工作/闪光科技2020年各季度研发费用分布图2.png')