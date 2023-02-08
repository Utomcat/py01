"""
NAME: custom_function.py <br/>
Description: Python 自定义函数 <br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2023-02-08
"""


# 自定义函数 hello(), 用于输出 Hello World! 字符串
def hello():
    print("Hello World!")


# 调用结果,输出: Hello World!
hello()


# 自定义函数 max_number() 比较两个数, 并返回较大的数
def max_number(a, b):
    if a > b:
        return a
    else:
        return b


# 调用结果,输出: 6
print(max_number(3, 6))

'''
输出结果: 
调用改变函数之前地址:  140707971785512
函数内改变入参a值之前内存地址:  140707971785512
函数内改变入参a值之后内存地址:  140707971785800
'''


def change(a):
    # 指向的和传入的a 指向同一地址
    print("函数内改变入参a值之前内存地址: ", id(a))
    a = 10
    # 创建了新的对象,指向的是一个新的地址
    print("函数内改变入参a值之后内存地址: ", id(a))


a = 1
print("调用改变函数之前地址: ", id(a))
change(a)


'''
输出结果:
调用函数前函数外取值:  [10, 20, 30]
修改传入参数 my_list 前取值:  [10, 20, 30]
修改传入参数 my_list 后取值:  [10, 20, 30, [1, 2, 3, 4]]
调用函数后函数外取值:  [10, 20, 30, [1, 2, 3, 4]]
'''


def change(my_list):
    print("修改传入参数 my_list 前取值: ", my_list)
    my_list.append([1, 2, 3, 4])
    print("修改传入参数 my_list 后取值: ", my_list)
    return


my_list = [10, 20, 30]
print("调用函数前函数外取值: ", my_list)
change(my_list)
print("调用函数后函数外取值: ", my_list)
