from blackjack.card import Card
from blackjack.rank import Rank
from blackjack.suit import Suit


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.value += card.rank.value
        self.adjust_for_ace(card)
        self.cards.append(card)

    def adjust_for_ace(self, card):
        if card.rank == Rank.ACE:
            self.aces += 1
            if self.value > 21:
                self.value -= 10
