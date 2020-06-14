# coding=gbk
"""
目前定义的都是特殊方法
1. __eq__方法中对于两个操作数均为Vector2d的类型时适用，但是对于Vector(3, 4) == [3, 4]也适用
2. 缺少使用bytes()函数生成的二进制表示形式重建Vector2d实例
"""
import math
from array import array


class Vector2d:
    typecode = "d"  # 类属性，在Vector2d实例和字节之间转换时使用

    def __init__(self, x=0., y=0.):
        self.x = float(x)  # 转换成浮点数，今早捕获错误，以防调用Vector2d函数时传入不当参数
        self.y = float(y)

    def __iter__(self):  # 把实例变成可迭代的对象，才能使用拆包
        return (i for i in (self.x, self.y))

    def __repr__(self):
        """
        {!r}获取各个分量的表达形式，然后插值，构成一个字符串。因为是可迭代对象，所以*self才可以将
        x, y分量提供给format函数
        :return:
        """
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, *self)

    def __str__(self):  # 从一个可迭代的实例中得到元组，显示为一个有序对
        return str(tuple(self))

    def __bytes__(self):
        """
        先将typecode转换为字节序列
        再迭代实例得到一个数组，再把数组转换成字节序列
        :return:
        """
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        """
        为了快速比较所有分量，在操作数中构造元组
        :param other:
        :return:
        """
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))
