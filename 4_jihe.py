'''
    集合，集合是一个无序不重复的一个序列
'''

# 创建集合
set1 = {'baidu','toabao'}
set2 = set([4, 5, 6, 7])

# 空集合不能用{}，必须要用set()
set3 = set()

#添加元素
set2.add("facebook")

# update可以添加序列和字典的类似
set1.update({8,9},[10,11])
print(set1)

# 删除方法
set2.remove(7)
set2.discard(7) # 如果要素不存在，不会报错