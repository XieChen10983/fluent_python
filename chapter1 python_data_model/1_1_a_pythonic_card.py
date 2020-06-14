import collections
from random import choice

Card = collections.namedtuple("card", ['rank', 'suit'])
# ranks = [str(n) for n in range(2, 11)] + list('JQKA')
# print(ranks)
# suits = 'spades diamonds clubs hearts'.split()
# print(suits)


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
# rank_value = FrenchDeck.ranks.index(card.rank)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


deck = FrenchDeck()
for card in sorted(deck, key=spades_high):  # doctest: +ELLIPSIS
    print(card)
# print(my_card[0])
# print(my_card[-1])
# print(my_card[1])
# print(len(my_card))
# print("------------------------------")
# for _ in range(5):
#     print(choice(my_card))
# # beer_card = Card("7", "diamonds")
# # print(beer_card)
