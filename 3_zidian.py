'''
    字典（key:value)

'''
# 形态
tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}

# 使用内建函数 dict() 创建字典：
emptyDict=dict()
print(tinydict['name'])

# 修改
tinydict['name'] = 'wanggag'

#
# del tinydict['Name'] # 删除键 'Name'
# tinydict.clear()     # 清空字典
# del tinydict         # 删除字典