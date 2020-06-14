# coding=gbk
"""
1. 生成器表达式背后遵守了迭代器协议，可以逐个产出元素，而不是先建立一个完整的列表，然后再把这个列表传递
    到某个构造函数中。生成器表达式这种方式显然能够节省内存。
2. 生成器表达式的语法和列表推导差不多，只不过把方括号换成圆括号。
"""

"""-------------------------生成器表达式初始化元组---------------------------"""
symbols = "ldkjk"
ascii_symbols = tuple(ord(symbol) for symbol in symbols)
print(ascii_symbols)

"""-------------------------生成器表达式初始化数组---------------------------"""
import array
array1 = array.array("I", (ord(symbol) for symbol in symbols))
print(array1)

"""-------------------------生成器表达式计算笛卡尔积------------------------"""
colors = ["black", "white"]
sizes = ["L", "M", "S"]
for t_shirt in ([color, size] for color in colors for size in sizes):
    # 此处不会产生一个完整的列表，而是一个元素一个元素生成，当colors和sizes较大时，可以节省内存
    print(t_shirt)

colors = ("black", "white")
print(print("color %s/%s" % colors))

import numpy as np
