import pandas as pd
import warnings

# 关闭警告显示
warnings.filterwarnings('ignore')

# 读取并查看【商品销售数据.xlsx】工作簿的数据
data = pd.read_excel('工作\工作\商品销售数据.xlsx')
data.head(10)

# 查看数据的基本信息总结
data.info()

# 清洗【用户 ID】列的缺失值
data = data.dropna(subset=['用户 ID'])
# 查看清洗后的数据基本信息总结
data.info()

# 查找重复数据
data[data.duplicated()]

# 删除重复值
data = data.drop_duplicates()
# 查找清洗后的数据是否存在重复数据
data[data.duplicated()]

# 查看数据描述性统计的信息
data.describe()

# 筛选【数量】列大于 0 的数据
data = data[(data['数量'] > 0)]
# 查看数据描述性统计的信息
data.describe()

# 计算“总金额”
data['总金额'] = data['数量'] * data['价格']
data

# 按【订单号】和【用户 ID】分组后，获取【发货日期】列的最大值和【总金额】列的总和
grouped_data = data.groupby(['订单号', '用户 ID'], as_index=False).agg({'发货日期': 'max', '总金额': 'sum'})
grouped_data.head(10)

# 计算时间间隔  
today = '2012-01-01 00:00:00'
pd.to_datetime(today) - pd.to_datetime(grouped_data['发货日期'])

# 计算时间间隔
today = '2012-01-01 00:00:00'
grouped_data['时间间隔'] = (pd.to_datetime(today) - pd.to_datetime(grouped_data['发货日期'])).dt.days
grouped_data

# 按【用户 ID】分组后，获取【时间间隔】列的最小值、【订单号】列的数量，以及【总金额】列的总和
rfm_data = grouped_data.groupby('用户 ID', as_index=False).agg({'时间间隔': 'min', '订单号': 'count', '总金额': 'sum'})

# 修改列名
rfm_data.columns = ['用户 ID', '时间间隔', '总次数', '总金额']
rfm_data.to_excel('工作\工作\商品销售数据 rfm整理.xlsx')