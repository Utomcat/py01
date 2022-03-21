"""
CLASS_NAME: pythonLogicOperator.py <br/>
Description: 逻辑运算符测试 <br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2022 - 03 - 18
"""

# 定义变量
a = 1
b = 2
d = 1

# and 一假全假
print("a > b and a == d ? ", a > b and a == d)

# or 一真全真
print("a > b or a == d ? ", a > b or a == d)

# not 真假相反
print("a > b ? ", a > b)
print("not a > b ? ", not a > b)
