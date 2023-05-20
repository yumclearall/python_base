# 导入 apyori 模块下的 apriori 函数和 pandas 库
from apyori import apriori
import pandas as pd 

# 张三快餐店的部分销售数据，为了方便，这里直接将“购买的餐品”创建成列表形式。
data_1 = pd.DataFrame({"订单号": ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10'],
                    "购买的餐品": [['炒河粉', '可乐'], ['一碗香', '龙骨汤'], ['炒河粉', '鸡腿', '可乐'], ['炒河粉', '龙骨汤'], ['一碗香', '可乐'],
                                ['炒河粉', '可乐'], ['炒河粉', '麻辣牛肉', '可乐'], ['炒河粉', '青菜', '可乐'], ['一碗香', '青菜', '龙骨汤'], ['炒河粉']]})

# 创建变量 results，调用 apriori 函数并赋值给 results，将最小支持度设置为 0.15，最小置信度为 0.1
results = apriori(data_1,min_support=0.15,min_confidence=0.1)

# 查看变量 results
for result in results:
    print(result)


# 创建变量 results，调用 apriori 函数并赋值给 results，将最小支持度设置为 0.15，最小置信度为 0.1
results = apriori(data_1['购买的餐品'], min_support=0.15, min_confidence=0.1)

# 创建提取列表
extract_result = []

# 遍历结果数据
for result in results:
    # 获取支持度，并保留 3 位小数
    support = round(result.support,3)

    # 遍历 ordered_statistics 对象
    for rule in result.ordered_statistics :

        # 获取前件和后件并转成列表
        head_set = rule.items_base
        tail_set = rule.items_add

        # 跳过前件为空的数据
        if head_set == []:
            continue

        # 将前件、后件拼接成关联规则的形式
        related_catogory = str(head_set)+'→'+str(tail_set)

        # 提取提升度，并保留 3 位小数
        lift = round(rule.lift,3)
        
        # 提取置信度，并保留 3 位小数
        confidence = round( rule.confidence,3)

        # 将提取的数据保存到提取列表中
        extract_result.append([related_catogory, support, confidence, lift])

# 查看数据
extract_result


# 将数据转成 DataFrame 的形式
rules_data = pd.DataFrame(extract_result, columns=['关联规则', '支持度', '置信度', '提升度'])

# 查看数据
rules_data

# 导入 matplotlib 库
import matplotlib.pyplot as plt

# 设置字体
plt.rcParams['font.family'] = ['Source Han Sans CN']

# 设置画布尺寸
plt.figure(figsize=(20, 8))

# 画出以置信度为高度的柱状图，x 坐标为 rules_data.index-0.1，设置柱子的宽度为 0.2
plt.bar(rules_data.index-0.1, rules_data['置信度'], width=0.2)

# 画出以支持度为高度的柱状图，x 坐标为 rules_data.index+0.1，设置柱子的宽度为 0.2
plt.bar(rules_data.index+0.1, rules_data['支持度'], width=0.2)

# 设置名称分别为置信度、支持度的图例，设置字体大小(fontsize)为 15 
plt.legend(['置信度', '支持度'], fontsize=15)

# 设置标题为“关联规则的置信度、支持度柱状图”，设置字体大小(fontsize)为 20
plt.title('关联规则的置信度、支持度柱状图', fontsize=20)

# 设置刻度名称为对应的“关联规则”，刻度间隔为 rules_data.index
plt.xticks(rules_data.index, rules_data['关联规则'])

# 设置坐标轴标签
plt.xlabel('关联规则', fontsize=15)
plt.ylabel('数值', fontsize=15)