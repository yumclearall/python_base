import pandas as pd
# 设置列表
students_info = [['小蓝', '语文', '79'], 
                ['小邱', '数学', '83'], 
                ['小李', '英语', '92']]

# 使用列表创建 DataFrame 对象，同时设置列名
students_df = pd.DataFrame(students_info, columns=['姓名', '科目', '分数'])
print(students_df)
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
print(goods_df)
# 修改 goods_df 的列名
goods_df.columns = ['名称', '单价', '库存', '地址']
print(goods_df)