from collections import namedtuple
from random import sample

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in list(range(2, 11))] + list('JQKA')
    suits = 'Spades Diamonds Clubs Hearts'.split(' ')

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    # def __str__(self):
    #     return '{} of {}'.format(Card.rank, Card.suit)

    def shuffle(self):
        return sample(self._cards, k=len(self._cards))

if __name__ == "__main__":
    deck = FrenchDeck()
    print(deck.shuffle())
