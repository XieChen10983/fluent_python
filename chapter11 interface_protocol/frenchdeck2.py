# coding=gbk
import collections
from abc import ABC

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck2(collections.MutableSequence, ABC):
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __delitem__(self, key):
        del self._cards[key]

    def insert(self, key, value):
        self._cards.insert(key, value)


fren = FrenchDeck2()
print(fren[0])
