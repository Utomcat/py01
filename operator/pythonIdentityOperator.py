"""
CLASS_NAME: pythonIdentityOperator.py <br/>
Description: 身份运算符测试 <br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2022 - 03 - 18
"""

# 定义变量
a = 1
b = a
c = '1'

# is
print("a is b ", a is b)
print("a is c ", a is c)
print("b is c ", b is c)
print("id(a) ", id(a))
print("id(b) ", id(b))
print("id(c) ", id(c))

# is not
print("a is not b ", a is not b)
print("a is not c ", a is not c)
print("b is not c ", b is not c)

"""
is 和 == 的区别
is 用于判断两个变量引用对象是否为同一个(地址是不是同一个)
== 用于判断引用变量的值是否相等(值是不是同一个)
"""
