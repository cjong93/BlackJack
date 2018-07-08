import Deck
import Chips
import Hand

class Gameplay():
    def __init__(self):
        self.playing = True
#        self.deck = Deck.Deck()

if __name__ == '__main__':
    gameplay = Gameplay()
    chips = Chips.Chips()
    deck = Deck.Deck()
    deck.shuffle_deck()
    hand = Hand.Hand()

    #gameplay.deck.print_deck
    print("Welcome to Blackjack!")
    while(gameplay.playing):
        print(chips)
        
        hand.add_card(deck.deck[0])
#        print(deck.deck[0])
        hand.add_card(deck.deck[1])
#        print(deck.deck[1])

        for hand_cards in hand.return_hand():
            print(hand_cards)




        input_continue = ""
        while(input_continue.lower != "y".lower and input_continue.lower != "n".lower):
            input_continue = input("Will you continue to draw? (y/n)")
            if(input_continue.lower == "y".lower):
                print("y was selected")
                continue
            elif(input_continue.lower == "n".lower):
                print("thank you for playing")
                raise SystemExit
            else:
                print(f"{input_continue}")
                print("Invalid input, please select y or n")
        
        bet_selected = False
        while(bet_selected == False):
            chips.bet = int(input("How much will you bet?"))
            if(chips.bet < 0):
                print("you must bet more than 0")
            elif(chips.bet > chips.total):
                print("you don't have that many chips!")
            else:
                bet_selected = True
                print(f"You are now betting {chips.bet} number of chips!")

        player_won = input("Did you win or lose? (y/n)")
        if player_won.lower == "y".lower:
            player_won = True
        else:
            player_won = False
        print(player_won)
        if player_won:
            chips.win_bet()
        else:
            chips.lose_bet()
        