import random
import sys
import pandas as pd

number_of_turns = 1
class Deck():
    deck_stats = {"hairy_potatoe":5, "water_mallon":5, "defuse":4, "nope":5, "shuffle":5, "skip":5, "attack":5, "beard":5, "rainbow":5, "taco":5, 'future':5}
    #Deck.deck_stats.create_deck()
    #Deck.deck_stats.shuffle()
    def __init__(self):
    #create the deck
        self.discard_pile = []
        self.deck = self.create_deck()
        self.shuffle()
        deck = self.deck
        #deck = Deck.deck_stats
        #print(deck)


    def create_deck(self):
        deck = []
        #assign the number of cards for each type to a card (dict)
        #deck_stats = {"hairy_potatoe":5, "water_mallon":5, "defuse":6, "nope":5, "shuffle":5, "skip":5, "attack":5, "beard":5, "rainbow":5, "taco":5, 'future':5}
        #assign a value to each card for algorithmic purposes

        #create the card by putting the cards into a list then shuffle the list to randomise
        for card in Deck.deck_stats.keys():
          for i in range(0,Deck.deck_stats[card]):
            deck.append(card)
        return deck

    def add_exploding_kittens(self):
        '''
        adds the exploding kittens card at the end after distributing the cards to the player and the machine
        '''
        for i in range(4):
            self.deck.append("exploding_kitten")
        return

    def shuffle(self):
        '''
        randomise the deck or for when the shuffle card is played
        '''
        random.shuffle(self.deck)
        return self.deck

    def pickup(self):
        '''
        picks up the first card on the draw pile
        '''
        picked_up = self.deck.pop(0)
        #print(picked_up)
        return picked_up

    def deck_size(self):
        '''
        returns the length of the deck
        '''
        deck_size = len(self.deck)
        return deck_size

    def show_deck(self):
        '''
        gets the cards remaining in the deck
        '''
        #print(self.deck)
        return self.deck

    def show_discard_pile(self):
        '''
        #gets the first card in the discard discard_pile
        '''
        #print(self.discard_pile)
        return self.discard_pile

class Card():

    def __init__(self):
        pass

    def exploding_kitten(self):
        print("Kitten explodes because of nuclear meltdown!!!")
        return

    def defuse(self,previous_played_card):
        if (previous_played_card == "exploding_kitten"):
            print("Defused")
        return

    def future(self, previous_played_card, deck):
        #Lets you see the next 3 cards on deck
        next_three_cards = []
        if (previous_played_card == "future"):
            next_three_cards = deck[:3]
            print(next_three_cards)
        return

    def shuffle(self):
        Deck().shuffle()
        return

    def nope(self):
        '''CAN ONLY BE PLAYED WHEN IT'S ANOTHER PLAYER'S TURN'''
        #stops the effect of the played cards
        #if nope is not true then other cards work
        return True

    def skip(self):
        '''
        skips the turn so you don't need to draw a card
        change the playing turn object?
        '''
        return True

    def attack(self):
        '''
        #take 2 turns
        '''
        number_of_turns = 2
        return number_of_turns

    def beard(self):
        '''
        Has no effect on it's own. Special effect only kicks in when there are 2 or 3 cards
        '''
        print("beard")
        return

    def water_mallon(self):
        '''
        Has no effect on it's own. Special effect only kicks in when there are 2 or 3 cards
        '''
        print("water_mallon")
        return

    def card_effect(self,nope):
        #Defines the effect on cards. Example, defuse effect is active initially but if nope is played
        #then the defuse effect becomes inactive
        if (nope == True):
            return False
        return True



class Computer(Deck):

    def __init__(self, computer_hand):
        #print(Deck.deck_stats)
        '''Computer object still needs to access the same deck as the players'''
        self.computer_hand = computer_hand
        return

    def play_card(self, card_played):
        #Computer AI plays a card based on card_played by player
        #decides to draw or play card

            #keeps drawing card until there are only 16 cards Left
        #if Computer has no diffuse use 3 cards to get a defuse card from player
        #use future if there are 20cards or less
        #draw card
        #plays defuse if drawn exploding kittens

        return




class Player(Deck, Card, Computer):
    deck = Deck()
    def __init__(self):
    #create player's initial hand, must have a defuse, get cards from the deck, at the beginning no one can draw an exploding kitten
        self.player_hand = ["defuse"]
        self.deck = Deck()
        computer_hand = ["defuse"]
        for i in range(12):
            self.draw_card()
        computer_hand += self.player_hand[7:]
        print("Computer Hand: ")
        print(computer_hand)
        self.player_hand = self.player_hand[:7]
        print("Player Hand: ")
        print(self.player_hand)
        Computer.__init__(self,computer_hand)
        self.deck.add_exploding_kittens()
        self.deck.shuffle()

    def draw_card(self):
    #draw pile reduces by one
    #deck.create_deck()
    #deck.shuffle()
        self.player_hand.append(self.deck.pickup())
        deck_size = self.deck.deck_size()
        return self.player_hand

    def play_card(self,card_to_play):
        '''plays a card in hand, the player chooses which card to play. Card 0 is the first card, card 1 is the second card and so on
        1.Convert card_to_play type from list of strings to list of integers
        2.Then play card
        '''
        #Check the selected cards to play are identical if multiple cards are selected
        #if two of a kind is played pick a random card from the opponent
        #if three of a kind is played specify a card to pick from the opponent
        cards_to_play = []
        for i in card_to_play:
            cards_to_play.append(int(i))
        print(len(cards_to_play))
        for i in range(len(cards_to_play)):
            self.deck.discard_pile.append(self.player_hand[cards_to_play[i]])
            print(self.deck.discard_pile[-1])
        #self.deck.discard_pile.append(self.player_hand[card_to_play])
        #print(self.deck.discard_pile[0])
        if (self.deck.discard_pile[0] == "defuse"):
            Card().defuse(self.deck.discard_pile[0])
        elif (self.deck.discard_pile[0] == "future"):
            Card().future(self.deck.discard_pile[0],self.deck.deck)
        elif (self.deck.discard_pile[0] == "shuffle"):
            Card().shuffle()
        elif (self.deck.discard_pile[0] == "skip"):
            self.player_turn(Card().skip())
        elif (self.deck.discard_pile[0] == "nope"):
            pass
        elif (self.deck.discard_pile[0] == "attack"):
            Card().attack()
        #Code for when two of a kind or three of a kind
        return

    def show_cards(self):
        #show all cards in hand
        print(self.player_hand)
        return self.player_hand

    def show_deck(self):
        #Shows all cards remaining in deck
        print self.deck.show_deck()
        return

    def show_discard_pile(self):
        #print self.deck.discard_pile
        return self.deck.discard_pile

    def player_turn(self,skip):
        if (skip == True):
            print("False")
            return False
        return True

    def duplicates(self,player_hand):
        two_of_a_kind = set()
        three_of_a_kind = set()
        for i in player_hand:
            if player_hand.count(i) == 2:
                two_of_a_kind.add(i)
                print(list(two_of_a_kind))
            return
            if player_hand.count(i) == 3:
                three_of_a_kind.add(i)
                print(list(three_of_a_kind))
        return





class A(object):
    def a1(self):
        """ This is an instance method. """
        print "Hello from an instance of A"

    @classmethod
    def a2(cls):
        """ This a classmethod. """
        print "Hello from class A"

class B(object):
    def b1(self):
        print A().a1() # => prints 'Hello from an instance of A'
        print A.a2() # => 'Hello from class A'


#bb = B()
#bb.b1()



player = Player()
#create machine hand which needs to be the same deck as the player's deck
if __name__ == "__main__":
    for i in range(number_of_turns):
        card_to_play = raw_input("Which card or cards do you want to play? Enter the number: ")
        card_to_play = card_to_play.split()
        print(card_to_play)
        player.play_card(card_to_play)
        player.show_discard_pile()
    player.show_deck()
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    #machine = Computer()


# a = Deck()
# a.show_deck()
# a.show_discard_pile()
