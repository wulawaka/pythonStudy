'''
   栈实现方法，目前是O(n)，
'''

class Strack:
    def __init__(self):
        self.items=[]    #这一步用deque()，self.items=deque(),这样就是O(1)
    
    def push(self,item):
        self.items.append(item)  
    
    def pop(self):
        if len(self.items) == 0:
            return "空栈"
        else:
           num = len(self.items) - 1
           lieve = self.items[num]
           del self.items[num]
           return "出队参数 %d ." % (lieve)
        
q = Strack()
q.push(1)
q.push(3)
q.push(4)
q.push(5)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
