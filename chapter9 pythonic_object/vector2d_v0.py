# coding=gbk
"""
Ŀǰ����Ķ������ⷽ��
1. __eq__�����ж���������������ΪVector2d������ʱ���ã����Ƕ���Vector(3, 4) == [3, 4]Ҳ����
2. ȱ��ʹ��bytes()�������ɵĶ����Ʊ�ʾ��ʽ�ؽ�Vector2dʵ��
"""
import math
from array import array


class Vector2d:
    typecode = "d"  # �����ԣ���Vector2dʵ�����ֽ�֮��ת��ʱʹ��

    def __init__(self, x=0., y=0.):
        self.x = float(x)  # ת���ɸ����������粶������Է�����Vector2d����ʱ���벻������
        self.y = float(y)

    def __iter__(self):  # ��ʵ����ɿɵ����Ķ��󣬲���ʹ�ò��
        return (i for i in (self.x, self.y))

    def __repr__(self):
        """
        {!r}��ȡ���������ı����ʽ��Ȼ���ֵ������һ���ַ�������Ϊ�ǿɵ�����������*self�ſ��Խ�
        x, y�����ṩ��format����
        :return:
        """
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, *self)

    def __str__(self):  # ��һ���ɵ�����ʵ���еõ�Ԫ�飬��ʾΪһ�������
        return str(tuple(self))

    def __bytes__(self):
        """
        �Ƚ�typecodeת��Ϊ�ֽ�����
        �ٵ���ʵ���õ�һ�����飬�ٰ�����ת�����ֽ�����
        :return:
        """
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        """
        Ϊ�˿��ٱȽ����з������ڲ������й���Ԫ��
        :param other:
        :return:
        """
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))
