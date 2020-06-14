# coding=gbk
"""
classmethod改变了调用方法的方式，因此类方法的第一个参数是类本身，而不是类实例
"""
from vector2d_v0 import Vector2d as V


class Vector2d(V):

    def __init__(self):
        super(Vector2d, self).__init__()

    @classmethod  # 类方法使用classmethod装饰器装饰
    def frombytes(cls, octets):  # 不用传入self参数；相反，需要通过cls转入类本身
        typecode = chr(octets[0])  # 从第一个字节中读取typecode
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
