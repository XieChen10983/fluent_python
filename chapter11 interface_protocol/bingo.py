# coding=gbk
import random
from tombola import Tombola


class BingoCage(Tombola):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")

    def __call__(self, *args, **kwargs):
        self.pick()

    def get(self):
        return self._items


bingo = BingoCage([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(bingo.pick())
print(bingo.get())
