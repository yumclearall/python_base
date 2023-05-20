import pandas as pd
# 读取练习数据，文件路径为'./工作/test_data.csv'，编码格式为'u
mask_data = pd.read_csv('工作/mask_data.csv',encoding='utf-8')
# 查找 mask_data 中的重复行
mask_data.duplicated()
# 查看 mask_data 中的重复数据
print(mask_data[mask_data.duplicated()])
# 直接删除所有重复值
mask_data = mask_data.drop_duplicates()
# 查看 mask_data 中的重复数据
print(mask_data[mask_data.duplicated()])
# 查看清洗后的基本信息总结
mask_data.info()

# 查看 mask_data 的描述性统计信息
mask_data.describe()
# 查看单价小于等于 200 的数据
mask_data[mask_data['单价'] <= 200]
# 查看 mask_data 的描述性统计信息
mask_data.describe()
# 筛选订单量大于 0 的数据
mask_data=mask_data[mask_data['订单量']>0]
# 查看 mask_data 的描述性统计信息
mask_data.describe()

# 转换日期数据，并设置对应的日期格式
date_data = pd.to_datetime(mask_data['日期'], format = '%Y-%m-%d')
# 提取日期数据中的月份信息
month_data = date_data.dt.month
# 将月份数据添加到原数据中
mask_data['月份'] = month_data
# 查看原数据
mask_data

# 保存清洗干净的数据
mask_data.to_csv('工作/mask_data_clean.csv', encoding = 'utf-8')

# 保存清洗干净的数据，并取消写入行索引
mask_data.to_csv('工作/mask_data_clean.csv', index = False)



# 查看'明细'一列含有缺失值的数据
#exercise[exercise['明细'].isna()]
# 替换'明细'中的缺失值为'矿泉水'
#exercise['明细'] = exercise['明细'].fillna('矿泉水')
# 查看exercise的基本信息总结
#exercise.info()



