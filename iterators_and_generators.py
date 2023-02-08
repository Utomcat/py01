"""
NAME: iterators_and_generators.py <br/>
Description: Python迭代器和生成器 <br/>
@author ranyk <br/>
@version V1.0 <br/>
@date 2023-02-08
"""
import sys

# 声明 List 对象
li = [1, 2, 3, 4]
# 创建迭代器对象
it = iter(li)
# 输出迭代器对象, 输出结果: <list_iterator object at 0x000001FDC81A7FD0>
print(it)
# 输出迭代器的下一个元素,输出结果: 1
print(it.__next__())
# 输出迭代器的下一个元素,输出结果: 2
print(it.__next__())
# 使用 for 循环遍历迭代器对象,由于上面已经输出过迭代器对象的前两个元素,故此处输出迭代器的元素只有后两个,输出结果为: 3 4
for item in it:
    print(item, end=" ")


class MyNumbers:
    """
    创建数字迭代器类,初始值为 1,逐步增加 1
    """

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


my_class = MyNumbers()

my_iter = iter(my_class)
'''
输出结果为: 
1
2
3
4
'''
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
