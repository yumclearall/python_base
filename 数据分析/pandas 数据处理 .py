# 导入 pandas 库并将其简化为 pd
import pandas as pd
# 读取口罩厂数据，文件路径为 './工作/mask_data.csv'，并将编码格式设置为 'utf-8'
mask_data =pd.read_csv('./工作/mask_data.csv',encoding='utf-8')
# 查看 mask_data
print(mask_data)

# 查看 mask_data 的基本信息总结
print(mask_data.info())

# 查看 mask_data 的缺失)值
print(mask_data.isna())

# 查看数据后 5 行
print(mask_data.tail())

# 删除所有缺失值
mask_data = mask_data.dropna()
# 查看数据基本信息总结
print(mask_data.info())

