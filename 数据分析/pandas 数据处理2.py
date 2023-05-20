import pandas as pd
# 读取练习数据，文件路径为'./工作/test_data.csv'，编码格式为'utf-8'
test_data = pd.read_csv('工作/mask_data.csv',encoding='utf-8')
# 查看 test_data 的基本信息总结
print(test_data.info())
# 删除'品牌', '上牌时间', '里程数(km)', '保值率'四列数据缺失的行
test_data=test_data.dropna(subset=['品牌', '上牌时间', '里程数(km)', '保值率'])
# 查看 test_data 的基本信息总结
print(test_data.info())