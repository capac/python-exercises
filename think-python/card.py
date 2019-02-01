import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        dict_ranks = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
        dict_suits = {0: 'Clubs', 1: 'Diamonds', 2: 'Hearts', 3: 'Spades'}
        return '{0:s} of {1:s}'.format(dict_ranks[self.rank], dict_suits[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck(Card):
    def __init__(self):
        cards = [Card(rank, suit) for suit in range(4) for rank in range(2, 15)]
        self.cards = random.sample(cards, k=len(cards))

    def remove_card(self):
        return self.cards.pop()

    def add_cards(self, card):
        return self.cards.append(card)

    def __str__(self):
        return '\n'.join([str(card) for card in self.cards])

    # def shuffle(self):
    #     return [str(card) for card in random.sample(self.cards, len(self.cards))]

    def move_cards(self, hand, num):
        for n in range(num):
            hand.add_cards(self.remove_card())
        return hand


class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label


if __name__ == "__main__":
    # card = Card(13, 2)
    # print(card)
    deck = Deck()
    # print(deck)
    # new_deck = deck.shuffle()
    # print(new_deck)
    # print(deck.shuffle())
    # print(len(deck.shuffle()))
    hand = Hand()
    print(deck.move_cards(hand, 6))
