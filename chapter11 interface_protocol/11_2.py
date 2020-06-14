# coding=gbk
"""
FrenchDeck类不支持洗牌(shuffle)
"""
import collections


Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
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


my_cards = FrenchDeck()
abc = list(range(10))
from random import shuffle
shuffle(abc)
print(abc)
shuffle(my_cards)
print(my_cards[0])
