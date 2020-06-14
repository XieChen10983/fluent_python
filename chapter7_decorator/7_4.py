# coding=gbk
"""
此代码探究变量的作用域规则
"""
b = [6]  # 此b为全局变量
# print(id(b))
# b[0] += 1
# print(id(b))


def f1(a):
    print(a)
    print(b)


f1(3)


def f2(a):
    print(a)
    print(b)  # 此b在函数体中有赋值，为局部变量
    b = 9


f2(3)
