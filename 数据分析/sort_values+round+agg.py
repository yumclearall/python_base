import pandas as pd
goods_info = [
    ['巧克力', 77.675, '47箱', '广东佛山仓'], 
    ['牛奶', 58.755, '40箱', '广东揭阳仓'], 
    ['威化饼干', 7.385, '285盒', '广西南宁仓'], 
    ['火腿肠', 34.823, '20件', '广西柳州仓'], 
    ['巧克力', 62.648, '30箱', '广东揭阳仓'], 
    ['牛奶', 45.75, '12箱', '广西柳州仓'], 
    ['威化饼干', 5.235, '148盒', '广东佛山仓'], 
    ['火腿肠', 33.736, '28件', '广东佛山仓']
]
goods_df = pd.DataFrame(goods_info)
# 修改 goods_df 的列名
goods_df.columns = ['名称', '单价', '库存', '地址']
print(goods_df)

# 依照【单价】列的数据进行排序
newgoods_df = goods_df.sort_values(by='单价')
print(newgoods_df)

# 提取【单价】列的数据进行排序
newgoods_df['单价'].sort_values()

# 重置数据 sorted_goods 的行索引
reset_goods = newgoods_df.reset_index(drop=True)
print(reset_goods)

reset_goods['单价'] = round(reset_goods['单价'], 2)
print(reset_goods)

# 定义函数 new_func()
def new_func(data):
    number = data[:-1]
    return int(number)

# 使用 agg() 方法对【库存】列的数据进行切片处理
reset_goods['库存'] = reset_goods['库存'].agg(new_func)
print(reset_goods)

# 计算各食品的总库存量
reset_goods.groupby('名称')['库存'].sum()

#定义字典 dict_2
dict_2 = {
    '单价': 'mean', 
    '库存': 'sum'
}
# 同时计算各食品的平均单价和总库存量
reset_goods.groupby('名称').agg(dict_2)

# 创建一个 DataFrame 对象的数据
foods_df = pd.DataFrame({'食品名': ['肚脐饼', '水晶饺', '擂茶', '肚脐饼', '擂茶'], '单价': [2, 10, 12, 4, 20], '数量': [20, '-', 35, 37, '-'], '城市': ['潮州', '汕尾', '梅州', '深圳', '深圳']})
foods_df
# 定义函数，以替换【数量】列的“-”为 0
def replace_info(data):
    if data == '-':
        data = 0
    return data
# 使用 agg() 方法对【数量】列的内容进行替换
foods_df['数量'] = foods_df['数量'].agg(replace_info)
# 同时计算【单价】列的最小值和【数量】列的最大值
foods_df.groupby('食品名').agg({'单价': 'min', '数量': 'max'})




