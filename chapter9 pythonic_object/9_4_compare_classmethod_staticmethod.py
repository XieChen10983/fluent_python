# coding=gbk
"""

"""


class Demo:
    @classmethod
    def classmeth(cls, *args):
        return args

    @staticmethod
    def staticmeth(*args):
        return args


print(Demo.classmeth())
print(Demo.classmeth("spam"))
print(Demo.staticmeth("spam"))
