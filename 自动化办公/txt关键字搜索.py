import os

# 设置文件夹路径，获取文件夹下的所有文件名
path = 'c:/Users/86156/Desktop/.py/自动化办公/txt/工作文件夹/'
files_list = os.listdir(path)

# 设置需要查找的关键词
key_word = input("请输入要查找的关键词：")

# 打开结果文件
result_file = open('c:/Users/86156/Desktop/.py/自动化办公/txt/工作文件夹/demo_result.txt', 'a', encoding='utf-8')

# 循环处理每一个文件
for file_name in files_list:
    # 判断文件类型是否在文件名中
    if '.txt' in file_name:
        # 找到文件时先打印提示
        print("找到了文件：" + file_name)

        # 将文件夹路径和文件名拼接成该文件的相对路径
        target_file = path + file_name

        # 打开文件，读取文件内容，然后关闭文件
        file = open(target_file, 'r', encoding='utf-8')
        content = file.read()
        file.close()

        # 判断关键词是否在文件内容中
        if key_word in content:
            # 匹配到关键词时先打印提示
            print("妙啊，文件**{}**包含了关键词：{}".format(target_file, key_word))

            # 将包含关键词的文档的文件路径，写入结果文件。
            result_file.write(target_file + '\n')

# 关闭结果文件
result_file.close()