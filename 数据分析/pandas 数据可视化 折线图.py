import pandas as pd

# 导入matplotlib库的pyplot模块
from matplotlib import pyplot as plt
# 设置中文字体
plt.rcParams['font.family'] = ['Source Han Sans CN']

# 创建李健的数据
li_jian = pd.Series([80, 85, 89, 91, 88, 95],
                    index=['2月', '3月', '4月', '5月', '6月', '7月'])
# 查看li_jian
print(li_jian)

# 绘制单条折线图
li_jian.plot(kind='line', figsize=(7, 7), title='李健月考成绩')

# 绘制单条折线图
li_jian.plot(kind='line')

# 绘制李健成绩的折线图
li_jian.plot(use_index=False,xticks=[1,2,3],yticks=[90],rot=30,fontsize=20,figsize=(7,7))