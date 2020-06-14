# coding=gbk
"""
֮ǰ��ʵ�ֵ�Vector��ֻ�ܹ�����Vector�Ϳɵ������ݵ���ӣ�Vector+1��Vector+"ABC"��Ϊʵ�֡�
Ȼ��Ϊ������Ѽ�����͵ľ������ǲ��ܲ���other�����������ͣ�������Ԫ�ص����ͣ�Ӧ�ò����쳣������NotImplement
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
