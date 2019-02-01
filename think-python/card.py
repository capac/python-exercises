import random

class Card:
    def __init__(self, rank='2', suit='Clubs'):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '{0:s} of {1:s}'.format(self.rank, self.suit)


class Deck(Card):
    def __init__(self):
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        suits = 'Spades Hearts Diamonds Clubs'.split()
        self.cards = [str(Card(rank, suit)) for suit in suits for rank in ranks]

    def shuffle(self):
        return random.sample(self.cards, len(self.cards))


class Hand(Deck):
    def __init__(self, num):
        hand = []
        for n in range(num):
            hand.append(self.cards[n])
        return hand


if __name__ == "__main__":
    # card = Card('3', 'Diamonds')
    # print(card)
    # deck = Deck()
    # print(deck.shuffle())
    hand = Hand(5)
    print(hand)
