from blackjack.chips import Chips
from blackjack.dealer import Dealer
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.player import Player


class Play:

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.player.chips.take_bet()

        self.initialize_player()
        self.initialize_dealer()
        Play.show_some(self.player, self.dealer)

    def initialize_player(self):
        self.player.hand.add_card(self.deck.draw())
        self.player.hand.add_card(self.deck.draw())

    def initialize_dealer(self):
        self.dealer.hand.add_card(self.deck.draw())
        self.dealer.hand.add_card(self.deck.draw())

    def play(self):
        while input('Hit or stand (h/s)? ') == 'h':
            self.hit(self.player.hand)
            if self.evaluate():
                break
        else:
            self.evaluate()

        while self.dealer.hand.value <= 17:
            self.hit(self.dealer.hand)

        if self.dealer.hand.value > 21:
            Play.dealer_busts()
            self.player.chips.win_bet()
        elif self.dealer.hand.value > self.player.hand.value:
            Play.dealer_wins()
            self.player.chips.lose_bet()
        elif self.dealer.hand.value < self.player.hand.value:
            Play.player_wins()
            self.player.chips.win_bet()
        else:
            Play.push()

        print(f'You have {self.player.chips.total} chips')

        if 'y' == input('Do you want to play one more? (y/n)'):
            self.deck = Deck()
            self.player.reset()
            self.dealer.reset()
            self.initialize_player()
            self.initialize_dealer()
            Play.show_some(self.player, self.dealer)

            self.play()
        else:
            print('That was a pleasure. Good bye!')

    def evaluate(self):
        if self.player.hand.value > 21:
            Play.player_bust()
            self.player.chips.lose_bet()
            return True
        else:
            return False

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

    @staticmethod
    def player_bust():
        print('You loose!')

    @staticmethod
    def player_wins():
        print('You won!')

    @staticmethod
    def dealer_busts():
        print('Dealer busts, you won!')

    @staticmethod
    def dealer_wins():
        print('Dealer won!')

    @staticmethod
    def push():
        print('Push!')
