import matplotlib.pyplot as plt
import warnings
import pandas as pd

# 关闭警告显示
warnings.filterwarnings('ignore')
# 设置中文字体
plt.rcParams['font.family'] = ['Source Han Sans CN']

# 创建df数据
hairs = pd.DataFrame([['许钢铁', 6, 5], ['王铁锤', 8, 7], ['林志龙', 9, 7]], columns=['姓名', '去年发量', '今年发量'])

# 绘制基本柱状图
plt.bar(hairs.index, height=hairs['去年发量'], width=0.4)


plt.bar(hairs.index-0.2, height=hairs['去年发量'], width=0.4)


# 设置柱体宽度
bar_width = 0.4

# 使用两次 bar 函数画出两组条形图
plt.bar(hairs.index-bar_width/2, height=hairs['去年发量'], width=bar_width)
plt.bar(hairs.index+bar_width/2, height=hairs['今年发量'], width=bar_width)

# 纵坐标和横坐标标题
plt.ylabel('发量')  
plt.xlabel('姓名')
# 图形标题
plt.title('RY 工作室发量调查结果')
# 设置x轴的刻度名称
plt.xticks(hairs.index, hairs['姓名'])