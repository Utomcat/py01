"""
NAME: pythonLoopStructure.py <br/>
Description:  python 循环结构<br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2023-02-02
"""

# 使用 while 实现 1~100 的总和, 输出结果: 1~100 的总和为:  5050
i = 1
s = 0
while i <= 100:
    s = s + i
    i += 1
print("1~100 的总和为: ", s)

# 使用 while 实现无限循环
# var = 1
# while var == 1:
#     num = int(input("输入一个数字: "))
#     print("你输入的数字为: ", num)
# print("结束")

# while 循环使用 else
"""
执行输出结果: 
0  小于 5
1  小于 5
2  小于 5
3  小于 5
4  小于 5
5  大于或等于 5
"""
count = 0
while count < 5:
    print(count, " 小于 5")
    count += 1
else:
    print(count, " 大于或等于 5")

# while 简单语句组
# flag = 1
# while flag: print("输出flag: ", flag)
# print("程序结束")

# for 遍历列表
"""
执行输出结果: 
Baidu
Google
Runoob
Taobao
"""
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    print(site)

# for 遍历字符串
"""
执行输出结果: 
letter ==>  r
letter ==>  u
letter ==>  n
letter ==>  o
letter ==>  o
letter ==>  b
"""
word = 'runoob'
for letter in word:
    print("letter ==> ", letter)

# for...else 输出 0~6 结束后输出 Finally finished
'''
输出结果:
0
1
2
3
4
5
Finally finished!
'''
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# for...else 中间出现终止循环 break
'''
输出结果: 
循环数据 Baidu
循环数据 Google
菜鸟教程!
完成循环!
'''
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

# 在字母为 o 时 执行 pass 语句块
'''
执行结果: 
当前字母 : R
当前字母 : u
当前字母 : n
执行 pass 块
当前字母 : o
执行 pass 块
当前字母 : o
当前字母 : b
Good bye!
'''
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")
