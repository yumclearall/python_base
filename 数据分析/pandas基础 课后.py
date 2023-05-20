# 导入 pandas 库并将其简化为 pd
import pandas as pd
# 读取练习数据，文件路径为 './工作/exercise.csv'，文件编码为 'utf-8'
exercise = pd.read_csv('工作/保险案例.csv', encoding = 'utf-8')
# 查看 exercise
print(exercise)

# 查看exercise前5行数据
print(exercise.head())

# 查看exercise前8行数据
print(exercise.head(8))

