from openpyxl import load_workbook

# 打开【practice2.xlsx】工作簿
staff_wb = load_workbook('c:/Users/86156/Desktop/.py/自动化办公/openpyxl/practice2.xlsx')
# 按表名取表
staff_ws = staff_wb['下半年公司名单']

# 循环获取第四列（D列）的所有单元格对象
for col_cell in staff_ws['D']:
    # 如果为表头，则跳过本次循环
    if col_cell.value == '部门':
        continue
    # 打印原有的值
    print(col_cell.value)
    # 将原有的值修改为'战略储备部'
    col_cell.value='战略储备部'

# 将结果保存为【'practice2_result.xlsx'】
staff_wb.save('c:/Users/86156/Desktop/.py/自动化办公/openpyxl/practice2_results.xlsx')