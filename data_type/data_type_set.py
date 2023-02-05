"""
NAME: data_type_set.py <br/>
Description: Python 集合数据类型 <br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2023-02-02
"""

# 创建一个集合
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

# 打印集合 输出结果为: {'Baidu', 'Taobao', 'Facebook', 'Runoob', 'Google', 'Zhihu'}
print(sites)

# 成员测试 输出结果为: Runoob 在集合中
if 'Runoob' in sites :
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

# 打印集合 a 输出结果为: {'b', 'd', 'a', 'r', 'c'}
print(a)

# a 和 b 的差集 输出结果为: {'b', 'd', 'r'}
print(a - b)

# a 和 b 的并集 输出结果为: {'m', 'b', 'd', 'a', 'r', 'c', 'z', 'l'}
print(a | b)

# a 和 b 的交集 输出结果为: {'a', 'c'}
print(a & b)

# a 和 b 中不同时存在的元素 输出结果为： {'m', 'l', 'r', 'b', 'd', 'z'}
print(a ^ b)

# 创建空集合
c = set()

# 打印空集合 输出结果为: set()
print(c)
