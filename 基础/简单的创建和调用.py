class chinese:
    eye='black'
    def x(self):
        print('吃饭用筷子')
a=chinese()
print(a.eye)
a.x()
class Chinese:      # 创建一个类
    eye = 'black'

    def eat(self):
        print('吃饭，选择用筷子。')

wufeng = Chinese()   # 类的实例化
print(wufeng.eye)   # 实例调用类属性
wufeng.eat()  # 调用类中的方法（传参不用管self）
