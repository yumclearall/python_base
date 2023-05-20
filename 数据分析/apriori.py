# 导入 apyori 模块下的 apriori 函数
from apyori import apriori
# 创建4条快餐交易数据
orders = [['薯条', '可乐'], ['薯条', '可乐', '奶茶'], ['汉堡', '薯条', '可乐'], ['汉堡', '可乐']]
# 创建变量 results，调用 apriori 函数，传入参数：orders，最小支持度为 0.2，最小置信度为 0.7
results=apriori(orders,min_support=0.1,min_confidence=0.7)
# 查看变量 results
results
# 查看变量 results
for result in results:
    print(result)

results = apriori(orders, min_support=0.2, min_confidence=0.7)
# 遍历结果数据
for result in results:
    # 获取支持度,并保留3位小数
    support = round(result.support, 3)

    # 遍历ordered_statistics对象
    for rule in result.ordered_statistics:
        # 获取前件和后件并转成列表
        head_set = list(rule.items_base)
        tail_set = list(rule.items_add)

        # 跳过前件为空的数据
        if head_set == []:
                continue

        # 将前件、后件拼接成关联规则的形式
        related_catogory = str(head_set)+'→'+str(tail_set)

        # 提取置信度，并保留3位小数
        confidence = round(rule.confidence, 3)
        # 提取提升度，并保留3位小数
        lift = round(rule.lift, 3)

        # 查看强关联规则，支持度，置信度，提升度
        print(related_catogory, support, confidence, lift)

        