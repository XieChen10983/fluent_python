# coding=gbk
"""
֮ǰʵ�ֵ�Vector���ܹ�ʵ����ӹ��ܣ�Vector+tuple������tuple+Vector����׳�����
����ʵ���Ҽӹ��ܣ�__radd__��
"""
from example13_4 import Vector as V


class Vector(V):

    def __radd__(self, other):
        """self.__radd__ֱ��ί��self.__add__"""
        return self + other


if __name__ == "__main__":
    a = Vector((1, 2, 3))
    b = Vector((5, 6))
    c = (7, 8, 9, 10)
    print(b + a)
    print(a + c)
    # print(a+1)
