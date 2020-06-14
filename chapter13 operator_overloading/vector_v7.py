# coding=gbk
"""
重载标量乘法运算符 *
"""
from example13_10 import Vector as V
# from array import array
# import math
# import functools
# import operator
# import itertools
import numbers


class Vector(V):
    typecode = "d"

    # def __init__(self, components):
    #     self._components = array(self.typecode, components)

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            # print([n * numbers for n in self])
            return Vector(n * other for n in self)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __matmul__(self, other):
        try:
            return sum(a*b for a, b in zip(self, other))
        except TypeError:
            return NotImplemented

    def __rmatmul__(self, other):
        return self @ other

    def __imul__(self, other):

        return Vector(n * other for n in self)


if __name__ == "__main__":
    ax = Vector((4, 2, 3))
    ay = Vector((1, 2, 3))
    print(ax@ay)
    print(id(ax))
    ax += Vector((1, 1, 1))
    print(ax)
    print(id(ax))
    ax *= 2
    print(ax)
    print(id(ax))
