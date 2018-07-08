class Chips():

    def __init__(self):
        self.total = 100
        self.bet = 0

    def __str__(self):
        return str(f"You currently have {self.total} number of chips")

    def win_bet(self):
        print(f"Congradulations, you win {self.bet} number of chips!")
        self.total += self.bet
        print(f'Your balance is now {self.total}')

    def lose_bet(self):
        print(f"Aww, you lost {self.bet} number of chips!")
        self.total -= self.bet
        print(f'Your balance is now {self.total}')