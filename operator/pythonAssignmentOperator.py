"""
CLASS_NAME: pythonAssignmentOperator.py <br/>
Description:  赋值运算符测试<br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2022 - 03 - 16
"""

# 定义变量
a = 1
b = 2
c = 3

# 赋值运算符
# =
# 原来的 c 的值  3
#  = 后的 c 的值  1
print("原来的 c 的值 ", c)
c = a
print(" = 后的 c 的值 ", c)
print("\n")

# +=
# 原来的 c 的值  1
#  += 后的 c 的值  2
print("原来的 c 的值 ", c)
c += a
print(" += 后的 c 的值 ", c)
print("\n")

# -=
# 原来的 c 的值  2
#  -= 后的 c 的值  1
print("原来的 c 的值 ", c)
c -= a
print(" -= 后的 c 的值 ", c)
print("\n")

# *=
# 原来的 c 的值  1
#  *= 后的 c 的值  1
print("原来的 c 的值 ", c)
c *= a
print(" *= 后的 c 的值 ", c)
print("\n")

# /=
# 原来的 c 的值  1
#  /= 后的 c 的值  1.0
print("原来的 c 的值 ", c)
c /= a
print(" /= 后的 c 的值 ", c)
print("\n")

# %=
# 原来的 c 的值  1.0
#  %= 后的 c 的值  0.0
print("原来的 c 的值 ", c)
c %= a
print(" %= 后的 c 的值 ", c)
print("\n")

# **=
# 原来的 c 的值  0.0
#  **= 后的 c 的值  0.0
print("原来的 c 的值 ", c)
c **= a
print(" **= 后的 c 的值 ", c)
print("\n")

# //=
# 原来的 c 的值  0.0
#  //= 后的 c 的值  0.0
print("原来的 c 的值 ", c)
c //= a
print(" //= 后的 c 的值 ", c)
print("\n")

# :=
# 原来的 c 的值  0.0
#  := 后的 c 的值  True
# 小于五的数
# 下面这种写法会先计算 4 < 5 ,再将计算结果赋给变量 c , 等同于 c = (4 < 5)
print("原来的 c 的值 ", c)
if c := 4 < 5:
    print(" := 后的 c 的值 ", c)
    print("小于五的数")
else:
    print(" := 后的 c 的值 ", c)
    print("大于五的数")

# 原来的 c 的值  True
#  := 后的 c 的值  4
# 小于五的数
# 下面这种写法会先计算 c := 4 ,再计算 c < 5 , 等同于 (c = 4) < 5
print("原来的 c 的值 ", c)
if (c := 4) < 5:
    print(" := 后的 c 的值 ", c)
    print("小于五的数")
else:
    print(" := 后的 c 的值 ", c)
    print("大于五的数")
