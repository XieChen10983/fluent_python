# coding=gbk
"""
之前实现的Vector类能够实现左加功能：Vector+tuple，但是tuple+Vector则会抛出错误。
现在实现右加功能（__radd__）
"""
from example13_4 import Vector as V


class Vector(V):

    def __radd__(self, other):
        """self.__radd__直接委托self.__add__"""
        return self + other


if __name__ == "__main__":
    a = Vector((1, 2, 3))
    b = Vector((5, 6))
    c = (7, 8, 9, 10)
    print(b + a)
    print(a + c)
    # print(a+1)
