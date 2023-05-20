from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference

# 读取工作簿
wb = load_workbook('绘图/事业01部.xlsx')
# 读取工作簿中的活跃工作表
ws = wb.active
# 实例化 LineChart 类，得到 LineChart 对象, 并赋值给变量chart
chart=BarChart()
# 实例化 Reference 类，引用工作表的部分数据。将Reference对象赋值给变量data
data=Reference(worksheet=ws,min_row=3,max_row=9,min_col=1,max_col=5)
# 添加被引用的数据到 LineChart 对象
chart.add_data(data,from_rows=True,titles_from_data=True)
# 添加 LineChart 对象到工作表中，指定生成折线图的位置
ws.add_chart(chart, "C12")

# 引用"表头部分"单元格范围：第2行的第2列至第5列
fanwei=Reference(worksheet=ws,min_row=2,max_row=2,min_col=2,max_col=5)
# 设置类别轴的标签
chart.set_categories(fanwei)
# 设置 x 轴的标题为"季度"
chart.x_axis_title="季度"
# 设置 y 轴的标题为"利润"
chart.y_axis_title="利润"
# 给chart.style设置值（1到48的整数），推荐使用48
chart.style='40'
# 保存文件
wb.save('绘图/事业01部.xlsx')