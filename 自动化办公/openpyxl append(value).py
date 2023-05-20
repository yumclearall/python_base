from openpyxl import load_workbook

# 打开【公司人员名单.xlsx】工作簿
staff_wb = load_workbook('c:/Users/86156/Desktop/.py/自动化办公/openpyxl/公司人员名单.xlsx')
# 获取活动工作表
active_ws = staff_wb.active

info_list = ['S1911', '萧爵瑟', 3000, '内容']
info_tuple = ('S1912', '吴琐薇', 5000, '销售')

active_ws.append(info_list)
active_ws.append(info_tuple)
print(active_ws['C2'].value)

# 修改单元格对象C2的值为10000
active_ws['C2'].value = 1000

# 打印修改后的单元格对象C2的值
print(active_ws['C2'].value)

# 保存工作簿为【append_demo.xlsx】
staff_wb.save('openpyxl/abcd.xlsx')