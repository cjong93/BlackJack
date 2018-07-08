import Deck

class Gameplay():
    def __init__(self):
        self.playing = True
        self.deck = Deck.Deck()

if __name__ == '__main__':
    gameplay = Gameplay()
    gameplay.deck.print_deck
    print(gameplay.deck)