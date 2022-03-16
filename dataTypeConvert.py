# CLASS_NAME: dataTypeConvert.py <br/>
# Description: 数据类型转换 <br/>
# @author ranyk <br/>
# @version V1.0 <br/>
# @date 2022 - 03 - 15

# 声明字符串变量
a = "100"
print("字符串变量 a 的初始值为: ", a, " 数据类型为: ", type(a))

# 1. 字符串转整型,int(X,base) 当 base 存在值时,意味着 X 代表的是 base 进制的数,而 int() 数据类型转换为将 base 进制的数转换为 十进制 数
print("字符串变量 a 转为int类型值为: ", int(a), " 数据类型为: ", type(int(a)))
# 16 进制的 100 转为 十进制 数为 256
print("字符串变量 a 转为int类型16进制值为: ", int(a, 16), " 数据类型为: ", type(int(a, 16)))
# 8 进制的 100 转为 十进制 数为 64
print("字符串变量 a 转为int类型8进制值为: ", int(a, 8), " 数据类型为: ", type(int(a, 8)))
"""
在 int(X,base) 进行类型转换时,当 base 存在值时, X 不能为数值,否则会抛出 int() can't convert non-string with explicit base 异常
print("字符串变量 a 转为int类型8进制值为: ", int(int(a), 8), " 数据类型为: ", type(int(a, 8)))
"""
"""
在 int(X,base) 进行类型转换时,当 base 存在值时, X 不能不符合 base进制数规则,
否则会抛出 invalid literal for int() with base XXXX 异常,如下代码抛 invalid literal for int() with base 8: '9'
print("字符串变量 a 转为int类型8进制值为: ", int("9", 8), " 数据类型为: ", type(int("9", 8)))
"""

# 2. 字符串转 boolean , 空字符串 None 数值0 转换为 boolean 的值为 False 其余为 True
print("字符串变量 a 转为boolean类型值为: ", bool(a), " 数据类型为: ", type(bool(a)))

# 3. 字符串转换 list
print("字符串变量 a 转为list类型值为: ", list(a), " 数据类型为: ", type(list(a)))

# 4. 字符串转换 set
print("字符串变量 a 转为set类型值为: ", set(a), " 数据类型为: ", type(set(a)))

# 5. 字符串转换 Tuple
print("字符串变量 a 转为tuple类型值为: ", tuple(a), " 数据类型为: ", type(tuple(a)))

# 6. 字符串转换 复数, 如果入参 a 为字符串, 那么函数 complex 则能传入第二个参数
print("字符串变量 a 转为complex类型值为: ", complex(a), " 数据类型为: ", type(complex(a)))

# 7. 字符串转换 float
print("字符串变量 a 转为float类型值为: ", float(a), " 数据类型为: ", type(float(a)))

# 8. dict 类型转换
b = [('a', 1), ('b', 2), ('c', 3)]
print("字符串变量 b 的初始值为: ", b, " 数据类型为: ", type(b))
print("字符串变量 b 转为dict类型值为: ", dict(b), " 数据类型为: ", type(dict(b)))

# 9. char 类型转换,该方法只能传入 int 类型数据,返回的是 当前整数对应的 ASCII 字符,python 3 中该方法支持 Unicode 字符,故 python 3 中没有 unichr() 函数
c = 100
print("字符串变量 c 的初始值为: ", c, " 数据类型为: ", type(c))
print("字符串变量 c 转为char类型值为: ", chr(c), " 数据类型为: ", type(chr(c)))

# 10. 字符转换为数值,该方法是将传入的字符转换为对应字符的十进制整数,方法 ord() 是  chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象,python 3 中无该方法）的配对函数
d = 'd'
print("字符串变量 d 的初始值为: ", d, " 数据类型为: ", type(d))
print("字符串变量 d 转为数值为: ", ord(d), " 数据类型为: ", type(ord(d)))

# 11. 将整数转换为十六进制字符串
e = 100
print("字符串变量 e 的初始值为: ", e, " 数据类型为: ", type(e))
print("字符串变量 e 转为十六进制字符串为: ", hex(e), " 数据类型为: ", type(hex(e)))

# 12. 将整数转换为八进制字符串
f = 100
print("字符串变量 f 的初始值为: ", f, " 数据类型为: ", type(f))
print("字符串变量 f 转为八进制字符串为: ", oct(f), " 数据类型为: ", type(oct(f)))
