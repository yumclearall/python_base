import pandas as pd

# 读取【StationeryOrder.csv】文件数据
data = pd.read_csv('工作\文具市场购物篮案例练习\工作\StationeryOrder.csv', encoding='gbk')
# 查看数据的前 10 行信息
data.head(10)

# 定义函数，将数据类型转换成列表
def conversion_data(s):
    return [s]


# 将“文具”列数据由“字符串”格式转变为“包含单个字符串的列表”格式
data['文具'] = data['文具'].agg(conversion_data)
# 将同一“id”的“包含单个字符串的列表”数据聚合为“包含多个字符串的列表”数据，并重置索引
new_data = data.groupby('id').sum().reset_index()
# 查看整理好的数据
new_data



# 步骤一：设置最小支持度、最小置信度以及最小提升度
# 步骤二：调用 apriori 函数，并从算法返回结果中提取前件（head_set）、后件（tail_set）、支持度（support）、置信度（confidence）、提升度（lift）数据
# 步骤三：筛选满足“后件中占比较多”、“支持度较大”条件的数据


from apyori import apriori
result=apriori(new_data['文具'],min_support=0.02,min_confidence=0.45,min_lift=1)
biaoge=[]
# 查看算法返回结果
for result1 in result:

    support=round(result1.support,3)
    for result2 in result1.ordered_statistics:
        items_base=list(result2.items_base)
        if items_base==[]:
            continue
        items_add=list(result2.items_add)
        item=str(items_base)+'-->'+str(items_add)
        confidence=round(result2.confidence,3)
        lift=round(result2.lift,3)
        print([item,support,confidence,lift])
        biaoge.append([item,support,confidence,lift])
biaoge2=pd.DataFrame(biaoge,columns=['前件-->后件','置信度','支持度','提升度'])
print(biaoge2)
biaoge2.to_csv('工作\文具市场购物篮案例练习\工作\StationeryOrder Apriori.csv')