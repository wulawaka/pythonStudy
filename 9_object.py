'''
    class:一个类
    def：类中方法
'''

# 简单的实例
class Myclass:
    i=123
    def f(self):
        return 'hello word'

x= Myclass()

# _init_()函数，相当于java的构造函数，但不支持重载，只能有一个
class two:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p = two('baidu',12)


print(x.i)
print(x.f())
print("two构造:"+p.name,p.age)


