# 导入csv模块
import csv
# 使用with open() as 打开'reader_demo.csv'，注意设置必要的参数
with open('c:/Users/86156/Desktop/.py/自动化办公/csv/员工发展基金确认表.csv', 'r', encoding='utf-8', newline='') as csv_file:
    # 将文件对象转换为reader对象
    csv_reader = csv.reader(csv_file)
    # 循环遍历reader对象，
    for csv_row in csv_reader:
        # 打印csv文件中的每一行内容
        print(csv_row)