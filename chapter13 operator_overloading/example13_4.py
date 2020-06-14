# coding=gbk
"""
ΪVector����Ӽӷ��������ϣ���ܹ�ʵ�ֳ�����ӣ�itertools.zip_longest����������ͬ������ӣ�Vector+tuple��
"""
from vector_v6 import Vector as V
import itertools


class Vector(V):

    def __add__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(x + y for x, y in pairs)


if __name__ == "__main__":
    a = Vector((1, 2, 3))
    b = Vector((5, 6))
    c = (7, 8, 9, 10)
    print(a+b)
    print(a+c)
