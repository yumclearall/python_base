import seaborn as sns
import pandas as pd

students_grade = pd.DataFrame({'李健': [80, 85, 89, 91, 88, 95],
                    '王聪': [95, 92, 90, 85, 75, 80],
                    '过凡': [90, 91, 92, 91, 90, 91]
                    }, index=['2月', '3月', '4月', '5月', '6月', '7月'])
# 绘制多条折线图
sns.lineplot(data=students_grade)

students_grade.plot(title='月度汇总表')