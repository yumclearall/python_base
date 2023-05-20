nums = int(input("输入一个100以内的数:"))
if nums >= 90:
    print("优")
elif nums >= 80:
    print("良")
elif nums >= 70:
    print("中")
elif nums >= 60:
    print("及格")
elif nums <= 60 and nums >= 0:
    print("不及格")