class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise ValueError("You do not have enough money")
        else:
            self.balance -= amount

    def __str__(self):
        return 'Account owner: {} actual balance: ${}'.format(self.owner, self.balance)


account = Account('Kati', 100)

print(account)

try:
    account.withdraw(150)
except ValueError as e:
    print(e)

account.deposit(50)
account.withdraw(150)

print(account)
