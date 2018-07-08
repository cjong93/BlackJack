class Hand():
    def __init__(self):
        self.cards = []
        self.value = []
        self.aces = 0

    def __str__(self):
        str(f"you currently have the following cards")
        for card in self.cards:
            return str(card)

    def add_card(self, card):
        self.cards.append(card)
    
    def adjust_for_ace(self):
        for hand_cards in self.cards:
            if hand_cards[1] == 11:
                self.aces += 1

    def return_hand(self):
        return self.cards

    def return_value(self):
        pass