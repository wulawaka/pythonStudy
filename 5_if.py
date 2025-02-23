'''
    if语句
    以及python3新增的一个类似switch case功能：match...case
'''

# 基本格式
x=12
if x==11 :
    print('猜对了')
else :
    print('错误')

# match...case
match x:
    case 401:
        print("找不到了")
    case 12:
        print('找到了')