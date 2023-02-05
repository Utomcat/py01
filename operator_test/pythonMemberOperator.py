"""
CLASS_NAME: pythonMemberOperator.py <br/>
Description: 成员运算符测试 <br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2022 - 03 - 18
"""

# 定义变量
a = 10
b = 20
array = [6, 7, 8, 9, 10]

# a in array
if flag := (a in array):
    print("a 在数组 array 中, a in array 值为: ", flag)
else:
    print("a 不在数组 array 中, a in array 值为: ", flag)

# b in array
if flag := (b in array):
    print("b 在数组 array 中, b in array 值为: ", flag)
else:
    print("b 不在数组 array 中, b in array 值为: ", flag)

# a not in array
if flag := (a not in array):
    print("a 不在数组 array 中, a not in array 值为: ", flag)
else:
    print("a 在数组 array 中, a not in array 值为: ", flag)

# b not in array
if flag := (b not in array):
    print("b 不在数组 array 中, b not in array 值为: ", flag)
else:
    print("b 在数组 array 中, b not in array 值为: ", flag)
