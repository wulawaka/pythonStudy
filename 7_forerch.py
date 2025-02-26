'''
    for循环:
        break:跳出当前循环结束
        continue:重新开始循环，不执行下面的雨具
'''

sites = ["Baidu", "Google","Runoob","Taobao"]   
for site in sites:
    print(site)

# 打印字符串
word = 'runoob'
 
for letter in word:
    print(letter)

# 输出1-6
for number in range(1,6):
    print(number)
else :
    print("finally finished")