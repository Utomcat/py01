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

'''
&

2  ==> 0010
10 ==> 1010
&  ==> 0010
'''
print("a & b =", a & b)

# |
print("a | b =", a | b)

# ^
print("a ^ b =", a ^ b)

# ~ 向下取整
print(" ~a =", ~a)

# << ; n << m  ==> n * (2^m)
print("b << a =", b << a)

# >> ; n >> m ==> n / (2^m) 向下取整
print("b >> a =", b >> a)


# 5 ~5
'''
5 0101      
原码: 0101  
反码: 0101  
补码: 0101  

'''
print("5 的二进制为: ", bin(5), " 取反值为: ", ~5, " 取反的二进制为: ", bin(~5))
print("-5 的二进制为: ", bin(-5), " 取反值为: ", ~-5, " 取反的二进制为: ", bin(~-5))
