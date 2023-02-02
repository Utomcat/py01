"""
NAME: data_type_tuple.py <br/>
Description:  Python 元组数据类型<br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2023-02-02
"""

one = ('a', "b", 1, 2.0, True)
tow = (complex(1, 2), ['c', "d", 3, 4.0, False])

# 验证元组元素不可改变, 以下代码抛 TypeError: 'tuple' object does not support item assignment 错误
# one[0] = 'd'
# print(one[0])

# 输出元组 one , 输出结果为: ('a', 'b', 1, 2.0, True)
print(one)

# 输出元组第一个元素, 输出结果为: a
print(one[0])

# 截取元组 one 第 2~3 个元素, 输出结果为: ('b', 1)
print(one[1:3])

# 截取元组 one ,从第 3~最后一个元素, 输出结果为: (1, 2.0, True)
print(one[2:])

# 截取元组 one ,从第 2 个元素开始,增加步长为2(步长概念和 list 一致)截取, 输出结果为: ('b', 2.0)
print(one[1::2])

# 元组倒序输出, 输出结果为: (True, 2.0, 1, 'b', 'a')
print(one[-1::-1])

# 元组的连接, 输出结果为: ('a', 'b', 1, 2.0, True, (1+2j), ['c', 'd', 3, 4.0, False])
print(one + tow)

# 连续做 n 次操作,如下连续两次输出, 输出结果为: ('a', 'b', 1, 2.0, True, 'a', 'b', 1, 2.0, True)
print(one * 2)

# 空元组声明和初始化
three = ()

# 一个元素的元组声明和初始化
four = ('d',)

# 输出空元组,输出结果为: ()
print(three)

# 输出一个元素的元组,输出结果为: ('d',)
print(four)
