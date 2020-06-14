# coding=gbk
"""
classmethod�ı��˵��÷����ķ�ʽ������෽���ĵ�һ���������౾����������ʵ��
"""
from vector2d_v0 import Vector2d as V


class Vector2d(V):

    def __init__(self):
        super(Vector2d, self).__init__()

    @classmethod  # �෽��ʹ��classmethodװ����װ��
    def frombytes(cls, octets):  # ���ô���self�������෴����Ҫͨ��clsת���౾��
        typecode = chr(octets[0])  # �ӵ�һ���ֽ��ж�ȡtypecode
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
