from blackjack.chips import Chips
from blackjack.dealer import Dealer
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.player import Player


class Play:

    def __init__(self):
        self.deck = Deck()
        self.initialize_player()
        self.initialize_dealer()
        Play.show_some(self.player, self.dealer)
        self.player.chips.take_bet()

    def initialize_dealer(self):
        self.dealer = Dealer()
        self.dealer.hand.add_card(self.deck.draw())
        self.dealer.hand.add_card(self.deck.draw())

    def initialize_player(self):
        self.player = Player()
        self.player.hand.add_card(self.deck.draw())
        self.player.hand.add_card(self.deck.draw())

    def play(self):
        playing = True
        while playing:
            self.hit_or_stand(self.player.hand)

    def hit_or_stand(self, hand):
        while True:
            hit_or_stand = input('Hit or stand (h/s)? ')
            if hit_or_stand in ['h', 's']:
                if hit_or_stand == 'h':
                    self.hit(hand)
                break

    def hit(self, hand):
        hand.add_card(self.deck.draw())
        Play.show_some(self.player, self.dealer)

    @staticmethod
    def show_some(player, dealer):

        print('Dealer\'s cards:')
        print(*dealer.hand.cards[1:])
        print('First card is hidden...')
        print('Total value:' + str(dealer.hand.value))
        print('\n---------------------------\n')
        print('Player\'s cards')
        print(*player.hand.cards, sep=", ")
        print('Total value:' + str(player.hand.value))

    @staticmethod
    def show_all(player, dealer):
        print('Dealer\'s cards:')
        print(*dealer.hand.cards, sep=", ")
        print('First card is hided...')
        print('Total value:' + str(dealer.hand.value))
        print('\n---------------------------\n')
        print('Player\'s cards')
        print(*player.hand.cards, sep=", ")
        print('Total value:' + str(player.hand.value))

    def player_bust(self):
        pass

    def player_wins(self):
        pass

    def dealer_busts(self):
        pass

    def dealer_wins(self):
        pass

    def push(self):
        pass
