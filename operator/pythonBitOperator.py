"""
CLASS_NAME: pythonBitOperator.py <br/>
Description: 位运算操作符测试 <br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2022 - 03 - 18
"""

# 变量定义
a = 2
b = 10

# &
print("a & b =", a & b)

# |
print("a | b =", a | b)

# ^
print("a ^ b =", a ^ b)

# ~ 向下取整
print(" ~a =", ~a)

# << ; n << m  ==> n * (2*m)
print("b << a =", b << a)

# >> ; n >> m ==> n / (2*m) 向下取整
print("b >> a =", b >> a)
