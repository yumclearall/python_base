import csv

# 打开csv文件
with open('c:/Users/86156/Desktop/.py/自动化办公/csv/员工发展基金确认表.csv', 'r', encoding='utf-8', newline='') as csv_file:
    # 将文件对象转换为DictReader对象
    csv_reader = csv.DictReader(csv_file)
    # 获取表头
    headers = csv_reader.fieldnames
    # 打印表头
    print('表头：{}'.format(headers))
    # 遍历DictReader对象
    for csv_row in csv_reader:
        # 打印数据
        print(csv_row)