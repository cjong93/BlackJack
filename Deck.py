import random

class Deck():

    def __init__(self):
        self.suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        self.ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        self.values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

        deck = []
        for suit_x in self.suits:
            for ranks_x in self.ranks:
                deck.append((ranks_x+" of "+suit_x, self.values[ranks_x]))
        self.deck = deck
		
    def __str__(self):
        return str(self.deck)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def print_deck(self):
        print(self.deck)

if __name__ == '__main__':
    my_deck = Deck()
#    my_deck.shuffle_deck()
#    my_deck.print_deck()
    print(my_deck)