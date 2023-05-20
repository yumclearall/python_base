import pandas as pd
# 创建DataFrame对象
grade_df = pd.DataFrame({'班级': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
                         '性别': ['男', '男', '女', '女', '女', '男', '男', '男', '女', '女'],
                         '眼镜': ['是', '否', '是', '否', '是', '是', '是', '否', '否', '否'],
                         '成绩': [95, 90, 96, 92, 94, 85, 87, 80, 81, 86]})
# 查看grade_df
print(grade_df)

# 对班级进行分组聚合操作
grade_df1 = grade_df.groupby('班级')['成绩'].mean()
# 查看grade_df1
print(grade_df1)

# 求出不同性别学生数学成绩的中位数
grade_df2 =grade_df.groupby('性别')['成绩'].median()
# 查看grader_df2
grade_df2

# 求出不同性别学生数学成绩的总和
grade_df_sum = grade_df.groupby('性别')['成绩'].sum()
# 查看grader_df_sum
grade_df_sum

# 获取不同班级下不同性别的学生的平均分
grade_df3 = grade_df.groupby(['班级', '性别'])['成绩'].mean()
# 查看grade_df3
print(grade_df3)

# 获取不同性别的学生处于不同班级时的平均分
grade_df4 = grade_df.groupby(['性别','班级'])['成绩'].mean()
# 查看grade_df4
grade_df4

# 获取不同班级、不同性别、戴与不戴眼镜的学生的最高分
grade_df5 =grade_df.groupby(['班级','性别','眼镜'])['成绩'].max()
# 查看grade_df5
grade_df5

# 对grade_df5使用unstack函数
print(grade_df5.unstack())