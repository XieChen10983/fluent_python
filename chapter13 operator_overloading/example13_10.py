# coding=gbk
"""
之前所实现的Vector类只能够进行Vector和可迭代数据的相加，Vector+1，Vector+"ABC"均为实现。
然而为了遵守鸭子类型的精神，我们不能测试other操作数的类型，或者其元素的类型，应该捕获异常，返回NotImplement
"""
from example13_5 import Vector as V
import itertools


class Vector(V):

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except TypeError:
            # print("NotImplemented")
            return NotImplemented

    def __radd__(self, other):
        return self + other


if __name__ == "__main__":
    a = Vector((1, 2, 3))
    b = Vector((5, 6))
    c = (7, 8, 9, 10)
    print(b + a)
    print(a + c)
    print(a+"ABC")
