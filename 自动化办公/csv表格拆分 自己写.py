# 导入csv模块
import csv
lujing='c:/Users/86156/Desktop/.py/自动化办公/csv/员工发展基金确认表.csv'
cunf='c:/Users/86156/Desktop/.py/自动化办公/csv/员工发展基金文件夹_demo/'
# 设置员工发展基金确认表的路径
#with open(lujing,'w',econding='utf-8',newline='') as cun:
# 设置存放拆分结果文件的文件夹（员工发展基金文件夹）的路径。


# 打开员工发展基金确认表
with open(lujing,'r',encoding='utf-8',newline='') as biao:
    # 将文件对象转换为DictReader对象
    biaodu=csv.DictReader(biao)
    # 将csv对象的表头读取出来
    tous=biaodu.fieldnames

    # 循环处理确认表中除表头外的每一行数据
    for yg in biaodu:
        # 根据获取的员工名字拼接出新文件名
        wenjian=yg['\ufeff姓名']+'.csv'
        # 拼接新文件路径
        newlj=cunf+wenjian

        # 创建新文件并添加数据
        with open(newlj,'w',encoding='utf-8',newline='') as xie:
    # 将文件对象转换为DictReader对象)
            # 将文件对象转换为DictWriter对象
            xieru=csv.DictWriter(xie,fieldnames= tous)
            # 写入表头
            xieru.writeheader()
            # 写入数据
            xieru.writerow(yg)
print('完成')