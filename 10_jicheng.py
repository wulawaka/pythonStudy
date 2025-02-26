'''
    继承：
        子类（派生类）继承父类（基类），子类和父类必须在一个作用于内，
'''

class Teacher:
    name=''
    teach_object=''
    __t_id=0    #私有参数
    def __init__(self,n,to,td):
        self.name=n
        self.teach_object=to
        self.__t_id=td
    def speak(self):
        print("%s 是我的老师，她教 %s。"%(self.name,self.teach_object))

# 单继承
class student(Teacher) :
    myname=''
    def __init__(self,n,to,td,mn):
        Teacher.__init__(self,n,to,td)
        self.myname=mn
    def speak(self):
        print("%s 是我的老师，她教 %s 。我叫 %s 。"%(self.name,self.teach_object,self.myname))

s = student('ken','match',123,'wnag')
print(s.speak())

# 方法重写
class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')
 
class Child(Parent): # 定义子类
   def myMethod(self):
      print ('调用子类方法')
 
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法

