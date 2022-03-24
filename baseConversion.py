"""
CLASS_NAME: baseConversion.py <br/>
Description:  进制转换函数测试<br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2022 - 03 - 21
"""

# 定义 10 进制变量
a = 1314

two = '二'
eight = '八'
ten = '十'
sixteen = '十六'

# 10 进制转为 2 进制
result1 = bin(a)
print("%s进制数: %d 转为%s进制数其结果为: %s" % (ten, a, two, result1))

# 2 进制转为 10 进制
result2 = int(result1, 2)
print("%s进制数: %s 转为%s进制数其结果为: %d" % (two, result1, ten, result2))

print("\n")
# 10 进制转为 8 进制
result3 = oct(a)
print("%s进制数: %d 转为%s进制数其结果为: %s" % (ten, a, eight, result3))

# 8 进制转为 10 进制
result4 = int(result3, 8)
print("%s进制数: %s 转为%s进制数其结果为: %d" % (eight, result3, ten, result4))

print("\n")
# 10 进制转为 16 进制
result5 = hex(a)
print("%s进制数: %d 转为%s进制数其结果为: %s" % (ten, a, sixteen, result5))

# 16 进制转为 10 进制
result6 = int(result5, 16)
print("%s进制数: %s 转为%s进制数其结果为: %d" % (sixteen, result5, ten, result6))
