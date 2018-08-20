from blackjack.suit import Suit
from blackjack.rank import Rank
from blackjack.card import Card
import random


class Deck():

    def __init__(self):
        self.deck = Deck.generate_deck()
        random.shuffle(self.deck)

    @staticmethod
    def generate_deck():
        deck = []
        for suit in Suit:
            for rank in Rank:
                card = Card(rank, suit)
                deck.append(card)

        return deck

    def draw(self):
        return self.deck.pop()

    def __str__(self):
        return str([str(card) for card in self.deck])

