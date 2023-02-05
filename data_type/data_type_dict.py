"""
NAME: data_type_dict.py <br/>
Description: Python 字典数据类型 <br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2023-02-02
"""

# 定义空字典
dict = {}

# 打印空字典 输出结果为: {}
print(dict)
# 向字典中添加 key-value 键值对 one -- 1 - 菜鸟教程
dict['one'] = "1 - 菜鸟教程"
# 向字典中添加 key-value 键值对 o2 -- 2 - 菜鸟工具
dict[2] = "2 - 菜鸟工具"

# 打印字典 dict 输出结果为 {'one': '1 - 菜鸟教程', 2: '2 - 菜鸟工具'}
print(dict)

tiny_dict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

# 输出 dict 键为 'one' 的值 输出结果为: 1 - 菜鸟教程
print(dict['one'])
# 输出 dict 键为 2 的值 输出结果为: 2 - 菜鸟工具
print(dict[2])
# 输出完整的 tiny_dict 字典 输出结果为: {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(tiny_dict)
# 输出 tiny_dict 所有键 输出结果为: dict_keys(['name', 'code', 'site'])
print(tiny_dict.keys())
# 输出 tiny_dict 所有值 输出结果为: dict_values(['runoob', 1, 'www.runoob.com'])
print(tiny_dict.values())
