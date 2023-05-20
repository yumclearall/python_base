class Chinese:
    def __init__(self, greeting='你好', place='中国'):
        self.greeting = greeting
        self.place = place

    def greet(self):
        print('%s！欢迎来到%s。' % (self.greeting, self.place))

# 请为子类完成定制，代码量：两行。
class Cantonese(Chinese):
    def __init__(self,greeting ='你好',place='广东'):
        Chinese.__init__(self,greeting,place)
yewen = Cantonese()
yewen.greet()
