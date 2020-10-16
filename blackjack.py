import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

#Classes for the game

#class to create all the cards
class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck: #class for the deck

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp
    def shuffle(self): #to shuffle cards in the deck
        random.shuffle(self.deck)
    
    def deal(self): # to pick a card from the deck
        single_card = self.deck.pop()
        return single_card
    
class Hand: #shows the cards thar dealer and player has

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card): #add a card to the player or dealer hand
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -=10
            self.aces -=1


class Chips: #keeps track of chips

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


#define functions

def take_bet(chips) : #Ask for user's bet

    while True:
        try:
            chips.bet = int(input('How many chips do you want to bet? '))
        except ValueError:
            print("Sorry ! Please enter a valid Number: ")
        else:
            if chips.bet > chips.total:
                print("Your bet cannot exceed 100!")
            else:
                break


def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand): #function to hit or stand
    global playing

    while True:
        ask = input("Wiuld you like to hit or stand? Please enter 'h' or 's'")

        if ask[0].lower() == 'h':
            hit(deck, hand)
        elif ask[0].lower() == 's':
            print("Player stands, Dealer is playing.")
            playing = False
        else:
            print('Sorry I did not understand that!. Please try again!')
            continue
        break

def show_some(player, dealer):
    #print(" Dealer's Hand: ", *dealer.cards, sep='\n ')
    
    print(" Dealer's Hand: ")
    print(' <card hidden> ')
    print('')
    print("", dealer.cards[1])
    print("\n Players's Hand: ", *player.cards, sep='\n ')


def show_all(player, dealer):
    print(" Dealer's Hand: ", *dealer.cards, sep='\n ')
    print("Dealer's hand =",dealer.value)
    print("\n Players's Hand: ", *player.cards, sep='\n ')
    print("\n Players's Hand: ", player.value)


#game endings

def player_busts(player, dealer, chips):
    print('PLAYER BUSTS!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('PLAYER WINS!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('DEALER BUSTS!')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('DEALER WINS!')
    chips.lose_bet()

def push(player, dealer):
    print("it's push. Player and Dealer tie!")


#Gameplay
while True:
    print(' --- Welcome to the Game of BlackJack ---')

    #create and shuffle the deck
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #set up players chips
    player_chips = Chips()

    #ask player for bet
    take_bet(player_chips)

    #show cards
    show_some(player_hand, dealer_hand)

    while playing:
        #ask player to hit or stand
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)


        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

    print( "\n Player's winnings stand at", player_chips.total)

    new_game = input("\n Would you like to play again? Enter 'y' or 'n': ")
    if new_game.lower() =='y':
        playing = True
        continue
    else:
        print('Thanks for Playing. Have a nice day!')
        break