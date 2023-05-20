import pandas as pd
import warnings

# 关闭警告显示
warnings.filterwarnings('ignore')

# 读取并查看【商品销售数据.xlsx】工作簿的数据
rfm_data = pd.read_excel('工作\工作\商品销售数据 rfm整理.xlsx')

# 定义函数按照区间划分 R 值
def caculate_r(s):
    if s <= 100:
        return 5
    elif s <= 200:
        return 4
    elif s <= 300:
        return 3
    elif s <= 400:
        return 2
    else:
        return 1

# 对 R 值进行评分
rfm_data['R评分'] = rfm_data['时间间隔'].agg(caculate_r)
rfm_data

# 定义函数按照区间划分 F 值
def caculate_f(s):
    if s <= 5:
        return 1
    elif s <= 10:
        return 2
    elif s <= 15:
        return 3
    elif s <= 20:
        return 4
    else:
        return 5
# 对 F 值进行评分
rfm_data['F评分'] = rfm_data['总次数'].agg(caculate_f)
rfm_data

# 定义函数按照区间划分 M 值
def caculate_m(s):
    if s <= 2000:
        return 1
    elif s <= 4000:
        return 2
    elif s <= 6000:
        return 3
    elif s <= 8000:
        return 4
    else:
        return 5
# 对 M 值进行评分
rfm_data['M评分'] = rfm_data['总金额'].agg(caculate_m)
rfm_data

rfm_data.to_excel('工作\工作\商品销售数据 rfm整理2.0.xlsx')

# 计算 R评分、F评分、M评分的平均数
r_avg = rfm_data['R评分'].mean()
f_avg = rfm_data['F评分'].mean()
m_avg = rfm_data['M评分'].mean()

print('R评分的均值为：{}，F评分的均值为{},M评分的均值为{}'.format(r_avg, f_avg, m_avg))

# 将R评分、F评分、M评分 的数据分别与对应的平均数做比较
rfm_data['R评分'] = (rfm_data['R评分'] > r_avg) * 1
rfm_data['F评分'] = (rfm_data['F评分'] > f_avg) * 1
rfm_data['M评分'] = (rfm_data['M评分'] > m_avg) * 1
rfm_data

# 拼接R评分、F评分、M评分
rfm_score = rfm_data['R评分'].astype(str) + rfm_data['F评分'].astype(str) + rfm_data['M评分'].astype(str)
rfm_score

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
rfm_data['客户类型'] = rfm_score.replace(transform_label)
rfm_data.to_excel('工作\工作\商品销售数据 rfm整理3.0.xlsx')



