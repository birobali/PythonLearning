class Chips:
    def __init__(self):
        while True:
            try:
                self.total = int(input('Please enter the amount of chips: '))
                break
            except ValueError:
                print('Please enter a valid number!')

        self.bet = 0

    def take_bet(self):
        while True:
            try:
                bet = int(input(f'You have {self.total} chips, please take your bet: '))
                if bet > self.total:
                    raise ValueError('Your bet is bigger than your total!')
                break
            except ValueError as e:
                print(str(e))

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

