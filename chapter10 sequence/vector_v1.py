# coding=gbk
from array import array
import numbers
import reprlib
import math
import functools
import operator


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find("["):-1]
        return "Vector({})".format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    """
    ��������������ʵ�ְ���Vector��ʵ������Ƭ
    """
    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        cls = type(item)
        if isinstance(item, slice):
            return self._components[item]
        elif isinstance(item, numbers.Integral):
            return self._components[item]
        else:
            msg = "{cls.__name__} indices must be integers"
            raise TypeError(msg.format(cls=cls))

    shortcut_names = "xyztadf"

    def __getattr__(self, item):
        cls = type(self)
        if len(item) == 1:
            pos = cls.shortcut_names.find(item)
            if 0 <= pos <= len(self._components):
                return self._components[pos]
        msg = "{.__name__!r} object has no attribute {!r}"
        raise AttributeError(msg.format(cls, item))

    def __setattr__(self, key, value):
        cls = type(self)
        if len(key) == 1:
            if key in cls.shortcut_names:
                error = "readonly attribute {attr_name!r}"
            elif key.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ""
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=key)
                raise AttributeError(msg)
        super(Vector, self).__setattr__(key, value)

    """
    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes)
    """
    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)




v = Vector([0, 1, 2, 3, 4, 5, 6])
print(v[5])
print(v.x)
print(v.a)
