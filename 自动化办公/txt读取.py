# 设置要打开的txt文本文件的路径
target_file = 'c:/Users/86156/Desktop/.py/自动化办公/txt/工作文件夹/04_11_2020会议记录.txt'
# 打开目标txt文本文件
file = open(target_file, 'r', encoding='utf-8')
# 使用 文件对象.read() 方法读取文件内容
content = file.read()
# 打印文件内容
print(content)
# 关闭文件对象
file.close()