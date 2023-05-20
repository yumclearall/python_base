import pandas as pd
surname = pd.Series(['赵', '钱', '孙', '李'])
surname

# 创建Series对象
surname = pd.Series(['赵', '钱', '孙', '李'], index = ['学生1', '学生2', '学生3', '学生4'])
# 查看surname
print(surname)

# 创建Series对象
surname = pd.Series(['赵', '钱', '孙', '李'], index = ['学生1', '学生2', '学生3', '学生4'])
# 查看surname
print(surname)

# 创建 DataFrame 对象
new_df = pd.DataFrame({'年龄': [23, 22, 21],
                       '岗位': ['客服', '运营', '公关'],
                       '年购买量': [10, 15, 8]})
# 查看 new_df
print(new_df)

# 创建 DataFrame 对象
class_df = pd.DataFrame({'年龄': [25, 18, 23, 18],
                         '性别': ['女', '女', '女', '男']})
# 查看 class_df
print(class_df)

# 创建DataFrame对象
import numpy as np
class_df2 = pd.DataFrame(np.array([[25, '女'],
                                   [18, '女'],
                                   [23, '女'],
                                   [18, '男']]),
                         columns = ['年龄', '性别'],
                         index = [1, 2, 3, 4])
# 查看 class_df2
print(class_df2)

# 提取'年龄'这一列数据
class_df['年龄']

# 查看'年龄'这一列数据的类型
print(type(class_df['年龄']))

# 导入 csv 数据
my_data = pd.read_csv('c:/Users/86156/Desktop/.py/数据分析/工作/保险案例.csv', encoding = 'utf-8')
# 查看 my_data
print(my_data)

