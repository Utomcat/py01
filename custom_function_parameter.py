"""
NAME: custom_function_parameter.py <br/>
Description: Python 自定义函数参数 <br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2023-02-09
"""

'''
必要参数测试
'''


def print_me(msg):
    """
    打印字符串函数
    :param msg: 需要打印参数
    :returns: None 没有返回值
    """
    print("打印字符串: ", msg)
    return


# 调用 print_me() 函数,不传入参则会报 Parameter 'msg' unfilled 警告
# 执行调用会抛 TypeError: print_me() missing 1 required positional argument: 'msg' 异常
# print_me()
# 正常调用,打印结果为: 打印字符串:  aa
print_me("aa")

'''
关键字参数测试
'''
# 关键字参数调用, 打印结果为: 打印字符串:  bbb
print_me(msg='bbb')

'''
关键字参数测试,入参不按照定义时顺序传入测试
'''


def print_info(name, age):
    """
    打印传入的姓名和字符串
    :param name: 姓名参数值
    :param age: 年龄参数值
    :return: None 没有返回
    """
    print('姓名: ', name)
    print('年龄: ', age)
    return


# 打印结果:
# 姓名:  张三
# 年龄:  35
print_info(age=35, name='张三')

'''
默认参数测试
'''


def test00(a, b='str'):
    """
    默认参数测试方法
    :param a: 第一个参数
    :param b: 第二个参数值
    :return: None 没有返回值
    """
    print("第一个参数的参数值为: ", a)
    print("第二个参数的参数值为: ", b)
    return


# def test01(a='msg', b='bbb', c):
#     """
#     默认参数测试方法
#     :param a: 第一个参数
#     :param b: 第二个参数值
#     :return: None 没有返回值
#     """
#     print("第一个参数的参数值为: ", a)
#     print("第二个参数的参数值为: ", b)
#     return


"""
当传入的是 int 类型数据,而参数需要 String 类型数据时,调用处会报 Expected type 'str', got 'int' instead  警告,但是不影响函数执行
当传入参数存在多个时,如果前面一个参数指定了默认值,则后面的所有参数均需要指定默认值,否则会报 non-default parameter follows default parameter 错误,
执行时会抛 SyntaxError: non-default argument follows default argument 错误

输出结果为: 

调用结果打印: 
第一个参数的参数值为:  1
第二个参数的参数值为:  3
-----------------------
第一个参数的参数值为:  2
第二个参数的参数值为:  4
-----------------------
第一个参数的参数值为:  3
第二个参数的参数值为:  str
"""
print('调用结果打印: ')
test00(1, 3)
print('-----------------------')
test00(a=2, b=4)
print('-----------------------')
test00(a=3)

# print('调用test01结果打印: ')
# test01(1, 3)
# print('-----------------------')
# test01(a=2, b=4)
# print('-----------------------')
# test01(b=3)

'''
不定长参数测试
'''


def print_variable_length1(a,*var_tuple):
    """
    不定长参数测试方法一
    :param a: 必需参数值
    :param var_tuple: 不定长参数元组
    :return: None,无返回值
    """
    print("输出: ")
    print("a ==> ", a)
    print("*var_tuple ==> ", var_tuple)


# 不定长入参方法一调用:
'''
调用输出结果为：
输出: 
a ==>  1
*var_tuple ==>  (20, 50)
'''
print_variable_length1(1, 20, 50)
