"""
CLASS_NAME: formattedOutput.py <br/>
Description:  格式化输出<br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2022 - 03 - 21
"""

# 定义变量
name = '张三'
age = 26

# 字符串拼接方式输出
print('姓名: ' + name + ', 年龄: ' + str(age))

# 格式化输出
print("姓名: %s, 年龄: %d" % (name, age))

# 定义浮点型数据
money = 99999.919

# 浮点型数据格式化输出
print("姓名: %s, 年龄: %d, 月薪: %f" % (name, age, money))

# 指定浮点型数据保留小数位数
print("姓名: %s, 年龄: %d, 月薪: %.2f" % (name, age, money))

# 指定浮点型数据保留最小长度和小数位数
print("姓名: %s, 年龄: %d, 月薪: %6.1f" % (name, age, money))

# 定义一个列表
students = [{"name": "Wilder", "age": 27}, {"name": "Will", "age": 28}, {"name": "June", "age": 27}]

# (var) 辅助符操作
# 遍历列表,输出每个元素的姓名,年龄; %(name)s ==> name 属性字符串格式; %(age)d ==> age 整型格式;  % student 传入参数,列表中每次遍历的元素
for student in students:
    print('姓名: %(name)s ; 年龄: %(age)d ; ' % student)
