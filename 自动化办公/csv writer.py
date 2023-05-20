import csv
member_list = [
    ['邱大仁'],
    ['徐小刚', '陈知枫'],
    ['王晴', '廖雨']
    ]
with open('c:/Users/86156/Desktop/.py/自动化办公/csv/员工发展基金文件夹_demo/riterow_demo.csv','w',encoding='utf-8',newline='') as act:
    # 打开并创建'writerow_demo.csv'文件，注意参数的设置，获取文件对象
    acts=csv.writer(act)
    # 将文件对象转换为writer对象
    for member in member_list:
    # 循环遍历列表中的元素
        acts.writerow(member)
        # 将列表中的元素写入csv文件中