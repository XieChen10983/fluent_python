# coding=gbk
"""
[表达式(元素) for 元素 in 元素列表]  列表推导通常用来创建新的列表，如果其代码太长，就需考虑用for循环写了
列表推导在python3中不会受到同名变量的干扰，但是在python2中会受到推导表达式外的同名变量的干扰
"""

"""-----------------------------------列表推导和append的比较-------------------------------------"""
symbols = "$%^&*("
# codes = []
# for symbol in symbols:
#     codes.append(ord(symbol))
codes = [ord(symbol) for symbol in symbols]
print(codes)

"""-----------------------------------条件列表推导和map/filter的比较---------------------------------------"""
symbols = "LJLKGE$"
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 73]
# beyond_ascii = list(filter(lambda c: c > 73, map(ord, symbols)))
print(beyond_ascii)

"""-----------------------------------笛卡尔积-------------------------------------"""
colors = ["black", "white"]
sizes = ["S", "M", "L"]
# 这里（color，size）的先后顺序是后面for size in sizes for color in colors的先后顺序决定的，不是前面的决定的！！！
t_shirts = [(color, size) for size in sizes for color in colors]
print(t_shirts)
