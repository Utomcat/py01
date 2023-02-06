"""
NAME: python_derivation.py <br/>
Description: Python 推导式 <br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2023-02-03
"""

# 定义初始 name
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']

# 使用 List 推导式, 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
new_name = [name.upper() for name in names if len(name) > 3]
# 输出结果: ['ALICE', 'JERRY', 'WENDY', 'SMITH']
print(new_name)

# 使用 List 推导式, 计算 30 以内可以被 3 整除的整数
multiples = [i for i in range(30) if i % 3 == 0]

# 输出结果: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
print(multiples)

# 使用 Dict 推导式, 使用字符串及其长度创建字典
new_dict = {value: len(value) for value in names}

# 输出结果: {'Bob': 3, 'Tom': 3, 'alice': 5, 'Jerry': 5, 'Wendy': 5, 'Smith': 5}
print(new_dict)

# 使用 Dict 推导式, 同时使用条件,创建字典
new_dict1 = {key: len(key) for key in names if len(key) > 3}

# 输出结果: {'alice': 5, 'Jerry': 5, 'Wendy': 5, 'Smith': 5}
print(new_dict1)

# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典
dic = {x: x**2 for x in (2, 4, 6)}
# 输出结果为: {2: 4, 4: 16, 6: 36}
print(dic)

# 使用 Set 推导式, 计算数字 1,2,3 的平方数
new_set = {value**2 for value in {1, 2, 3}}

# 输出结果: {1, 4, 9}
print(new_set)

# 使用 Set 推导式, 判断不是 abc 的字母并输出
a = {x for x in 'abracadabra' if x not in 'abc'}

# 输出结果: {'r', 'd'}
print(a)

# 生成一个包含数字 1~9 的元组
b = (x for x in range(1, 10))

# 输出结果: <class 'generator'> ,所以元组推导式返回的是生成器对象
print(type(b))

# 输出结果: <generator object <genexpr> at 0x0000028D1D10E670>
print(b)

# 输出结果: (1, 2, 3, 4, 5, 6, 7, 8, 9) , 使用 tuple() 函数,可以直接将生成器对象转换成元组
print(tuple(b))
