from blackjack.hand import Hand
from blackjack.player import Player


class Dealer(Player):
    def __init__(self):
        self.hand = Hand()

    def reset(self):
        self.hand = Hand()
