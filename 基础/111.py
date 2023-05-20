#1
b = int(input("输入天数:"))
d = b % 365
c = int(b / 365)
print(c,"年,",d,"天")

#2
f = int(input("输入一个数:"))
j = 0
while(f != 0):
    j = j * 10
    j = j + f % 10
    f = int(f / 10)
print(j)