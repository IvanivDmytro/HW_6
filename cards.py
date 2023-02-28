import itertools
import random
from enum import Enum


_ranks = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
_suits = {
    'spades': '\u2660',
    'hearts': '\u2665',
    'diamonds': '\u2666',
    'clubs': '\u2663'
}

class SuitEnum(Enum):
    def __str__(cls):
        return cls.value


Suit = SuitEnum('Suit', _suits)



class Card:
    __slots__ = 'rank', 'suit'

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class CardDeckBase:
    cards = [Card(rank, suit) for rank, suit in itertools.product(_ranks, _suits)]

    def __len__(self):
        return len(self.cards)
    
    def __getitem__(self, position):
        return self.cards[position]


class FrenchDeck(CardDeckBase):
    pass


class CardDeck(FrenchDeck):
    def draw(self, n=1):
        """Return a list of n random cards"""
        return random.sample(self.cards, n)

    def fortune_tell(self, n=1):
        """Return a list of n random cards and their meaning"""
        cards = self.draw(n)
        meanings = [
            "This card represents your past",
            "This card represents your present",
            "This card represents your future",
        ]
        results = []
        for i, card in enumerate(cards):
            results.append(f"Card {i+1}: {card.rank}{card.suit}\nMeaning: {meanings[i]}")
        return results


if __name__ == '__main__':
    deck = CardDeck()
    print(deck.fortune_tell(3))
