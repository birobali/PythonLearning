from blackjack.chips import Chips
from blackjack.hand import Hand


class Player:

    def __init__(self):
        self.hand = Hand()
        self.chips = Chips()

    def reset(self):
        self.hand = Hand()
