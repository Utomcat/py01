"""
CLASS_NAME: pythonConditionalStructure.py <br/>
Description:  python 条件结构<br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2022 - 03 - 24
"""
# if 条件判断
a = 7
while a < 8:
    if a % 2 == 0:
        print(a, "is even")
    else:
        print(a, "is odd")
    a += 1

# if 的基本用法
flag = False
name = 'lure'
# 判断变量是否为 python
if name == 'python':
    # 条件成立时设置标志为真
    flag = True
    # 并输出欢迎信息
    print('welcome boss')
else:
    # 条件不成立时输出变量名称
    print(name)

# elif用法
num = 5
if num == 3:
    # 判断num的值
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:
    # 值小于零时输出
    print('error')
else:
    # 条件均不成立时输出
    print('roadman')

# if语句多个条件
num = 9
# 判断值是否在0~10之间
if 0 <= num <= 10:
    # 输出结果: hello
    print('hello')

num = 10
# 判断值是否在小于0或大于10
if num < 0 or num > 10:
    print('hello')
else:
    # 输出结果: undefined
    print('undefined')

num = 8
# 判断值是否在0~5或者10~15之间
if (0 <= num <= 5) or (10 <= num <= 15):
    print('hello')
else:
    # 输出结果: undefined
    print('undefined')
