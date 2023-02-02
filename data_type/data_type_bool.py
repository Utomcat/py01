"""
NAME: data_type_bool.py <br/>
Description:  Python Boolean 数据类型<br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2023-02-02
"""

# 输出结果为: 判断 bool 和 int 是否属于同一数据类型:  True
print("判断 bool 和 int 是否属于同一数据类型: ", issubclass(bool, int))

# 使用 type() ,输出结果为 <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

# 判断 a 是否和 int 是同一种数据类型,输出结果为: a 是否和 int 是同一中数据类型:  True
a = 111
print("a 是否和 int 是同一中数据类型: ", isinstance(a, int))

# True == 1
if True == 1:
    print("True == 1 ?  True")
else:
    print("True == 1 ? False")

# 计算 True + 1 的结果,输出结果为: True + 1 = 2
print("True + 1 = ", True + 1)


# False == 0 False == 0 ?  True
if False == 0:
    print("False == 0 ?  True")
else:
    print("False == 0 ? False")

# 计算 False + 1 的结果,输出结果为: False + 1 = 1
print("False + 1 = ", False + 1)

# True is 1, 输出结果为: True is 1 ?  False ,但同时会抛出语法警告 SyntaxWarning: "is" with a literal. Did you mean "=="?
print("True is 1 ? ", True is 1)

# False is 0,输出结果为: False is 0 ?  False ,但同时会抛出语法警告 SyntaxWarning: "is" with a literal. Did you mean "=="?
print("False is 0 ? ", True is 0)

