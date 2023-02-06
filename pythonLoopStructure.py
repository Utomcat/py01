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
count = 0
while count < 5:
    print(count, " 小于 5")
    count += 1
else:
    print(count, " 大于或等于 5")

