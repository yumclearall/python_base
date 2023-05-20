import pandas  as pd
import matplotlib.pyplot as plt
import warnings

# 关闭警告显示
warnings.filterwarnings("ignore")

# 读取【air_new_data.xlsx】工作簿的数据
airline_data = pd.read_excel('工作/航空公司客户价值分析/air_new_data.xlsx')
# 查看数据的前 10 行信息
print(airline_data.head(10))

# 查看数据是否有空值
airline_data.isna()
# 去除“最近一次间隔天数”为空的记录
airline_notnull = airline_data.dropna(subset=['最近一次间隔天数'])
# 去除“近2年乘机次数”为空的记录
airline_notnull = airline_notnull.dropna(subset=['近2年乘机次数'])
# 去除“消费金额”为空的记录
airline_notnull = airline_notnull.dropna(subset=['消费总金额'])
# 打印出处理完缺失值后的数据基本信息
airline_notnull.info()

# 只保留消费金额非零的记录，同时去除年龄大于 100 的记录
airline = airline_notnull[airline_notnull['消费总金额'] != 0]
airline = airline[airline['年龄'] <= 100]

# 关键字段提取
airline = airline[['会员卡号', '最近一次间隔天数', '近2年乘机次数', '近2年乘机金额']]
# 保存清洗后的数据
airline.to_excel('工作/航空公司客户价值分析/air_new_data RFM1.xlsx', index=False)

import matplotlib.pyplot as plt

# 绘制 R 值的分值区间
plt.figure(figsize=(6, 6)) 
x = airline['最近一次间隔天数'].sort_values()
y = airline.index
plt.plot(x,y) 
plt.savefig('工作/航空公司客户价值分析/air_new_data R折线图.png')

# 定义函数按照区间划分标记 R 值
def caculate_r(s):
    if s <= 140:
        return 5
    elif s <= 280:
        return 4
    elif s <= 420:
        return 3
    elif s <= 560:
        return 2
    else:
        return 1

# 标记 R 值
airline['R评分'] = airline['最近一次间隔天数'].agg(caculate_r)
# 查看数据的前 10 行信息
airline.head(10)

# 绘制 F 值的分值区间
plt.figure(figsize=(6, 6))
x = airline['近2年乘机次数'].sort_values()
y = airline.index
plt.plot(x,y)
plt.savefig('工作/航空公司客户价值分析/air_new_data F折线图.png')


# 定义函数按照区间划分标记 F 值
def caculate_f(s):
    if s <= 4:
        return 1
    elif s <= 7:
        return 2
    elif s <= 10:
        return 3
    elif s <= 20:
        return 4
    else:
        return 5

# 标记 F 值
airline['F评分'] = airline['近2年乘机次数'].agg(caculate_f)

# 绘制 M 值的分值区间
plt.figure(figsize=(6, 6))
x = airline['近2年乘机金额'].sort_values()
y = airline.index
plt.plot(x,y)
plt.savefig('工作/航空公司客户价值分析/air_new_data M折线图.png')

# 定义函数按照区间划分标记 M 值
def caculate_m(s):
    if s <= 5000:
        return 1
    elif s <= 10000:
        return 2
    elif s <= 15000:
        return 3
    elif s <= 20000:
        return 4
    else:
        return 5

# 标记 M 值
airline['M评分'] = airline['近2年乘机金额'].agg(caculate_m)
# 查看数据的信息
airline


# 计算R评分、F评分、M评分的平均数
r_avg = airline['R评分'].mean()
f_avg = airline['F评分'].mean()
m_avg = airline['M评分'].mean()
print('R评分的均值为：{}，F评分的均值为{},M评分的均值为{}'.format(r_avg, f_avg, m_avg))

# 将R评分、F评分、M评分 的数据分别与对应的平均数做比较
airline['R评分'] = (airline['R评分'] > r_avg) * 1
airline['F评分'] = (airline['F评分'] > f_avg) * 1
airline['M评分'] = (airline['M评分'] > m_avg) * 1

# 拼接R评分、F评分、M评分
rfm_score = airline['R评分'].astype(str) + airline['F评分'].astype(str) + airline['M评分'].astype(str)

# 定义字典标记 RFM 评分档对应的用户分类名称
transform_label = {
    '111':'重要价值用户',
    '101':'重要发展用户',
    '011':'重要保持用户',
    '001':'重要挽留用户',
    '110':'一般价值用户',
    '100':'一般发展用户',
    '010':'一般保持用户',
    '000':'一般挽留用户'
}
# 将RFM评分替换成具体的客户类型
airline['客户类型'] = rfm_score.replace(transform_label)
# 查看数据的信息
airline.to_excel('工作/航空公司客户价值分析/air_new_data RFM2.xlsx')

# 可视化客户类型的分布
customer_data = airline.groupby('客户类型')['会员卡号'].count()
plt.rcParams['font.sans-serif'] = ['Source Han Sans CN']
plt.figure(figsize=(10, 10))
plt.bar(customer_data.index, customer_data)
plt.xlabel('客户类型', fontsize=12)
plt.ylabel('人数', fontsize=12)
plt.title('不同客户的数量分布', fontsize=16)
plt.savefig('工作/航空公司客户价值分析/air_new_data RFM柱状图.png')
