# coding=gbk
import random
from tombola import Tombola


class LotteryBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable)  # 可以满足元组等更多其他类型，并且创建副本，避免修改输入

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError("pick from empty LotterBlower")
        return self._balls.pop(position)

    def loaded(self):  # 覆盖抽象基类中的loaded方法，避免其调用inspect方法。
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))
