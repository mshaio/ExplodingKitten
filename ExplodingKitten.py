__metaclass__ = type
import random
import sys
#import pandas as pd
from terminaltextcolour import *

number_of_turns = 1
class Deck():
    '''
    The Deck class contains action required to form a deck
    '''
    def __init__(self):
        '''initialises the deck'''
        self.discard_pile = []
        self.deck = self.create_deck()
        self.shuffle()
        #deck = self.deck
        #print(deck)

    def create_deck(self):
        '''Creates the deck'''
        deck = []
        #assign a value to each card for algorithmic purposes
        deck_stats = {"hairy_potatoe":5, "water_mallon":5, "defuse":4, "nope":5, "shuffle":5, "skip":5, "attack":5, "beard":5, "rainbow":5, "taco":5, 'future':5, 'favour':5}
        #create the card by putting the cards into a list then shuffle the list to randomise
        for card in deck_stats.keys():
          for i in range(0,deck_stats[card]):
            deck.append(card)
        return deck

    def add_exploding_kittens(self):
        '''adds the exploding kittens card at the end after distributing the cards to the player and the machine'''
        for i in range(4):
            self.deck.append("exploding_kitten")
        return

    def shuffle(self):
        '''randomise the deck or for when the shuffle card is played'''
        random.shuffle(self.deck)
        #test = ["exploding_kitten", "nope", "exploding_kitten"]
        #self.deck = test + self.deck
        return self.deck

    def pickup(self):
        '''picks up the first card on the draw pile'''
        picked_up = self.deck.pop(0)
        #print(picked_up)
        return picked_up

    def deck_size(self):
        '''returns the length of the deck'''
        deck_size = len(self.deck)
        return deck_size

    def show_deck(self):
        '''gets the cards remaining in the deck'''
        #print(self.deck)
        return self.deck

    def show_discard_pile(self):
        '''gets the first card in the discard discard_pile'''
        #print(self.discard_pile)
        return self.discard_pile

class Card():
    '''
    Includes unique cards in the deck
    '''
    def __init__(self):
        pass

    def exploding_kitten(self):
        "Ends the game"
        print("Kitten explodes because of nuclear meltdown!!!")
        return

    def defuse(self,previous_played_card):
        '''Defuses the exploding kitten'''
        if (previous_played_card == "exploding_kitten"):
            print("Defused")
        return "defuse"

    def future(self, previous_played_card, deck):
        '''Lets you see the next 3 cards on deck'''
        next_three_cards = []
        if (previous_played_card == "future"):
            next_three_cards = deck[:3]
            print(next_three_cards)
        return

    def shuffle(self):
        '''Shuffles the deck'''
        Deck().shuffle()
        return

    def nope(self):
        '''CAN ONLY BE PLAYED WHEN IT'S ANOTHER PLAYER'S TURN'''
        #stops the effect of the played cards
        #if nope is not true then other cards work
        return True

    def skip(self):
        '''skips the turn so you don't need to draw a card change the playing turn object?'''
        return True

    def attack(self):
        '''#take 2 turns'''
        return "attack"

    def beard(self):
        '''Has no effect on it's own. Special effect only kicks in when there are 2 or 3 cards'''
        print("beard")
        return

    def water_mallon(self):
        '''Has no effect on it's own. Special effect only kicks in when there are 2 or 3 cards'''
        print("water_mallon")
        return

    def favour(self):
        '''Gives the other player a card of your choice'''
        print("favour")
        return "favour"

    def card_effect(self,nope):
        '''
        Defines the effect on cards. Example, defuse effect is active initially but if nope is played
        then the defuse effect becomes inactive
        '''
        if (nope == True):
            return False
        return True


class Player(Deck, Card):
    def __init__(self, deck):
        '''Create player's initial hand, must have a defuse, get cards from the deck, at the beginning no one can draw an exploding kitten'''
        self.player_hand = ["defuse"]
        self.deck = deck
        for i in range(6):
            self.draw_card()

    def draw_card(self):
        '''draw pile reduces by one'''
        self.player_hand.append(self.deck.pickup())
        return self.player_hand

    def play_card(self,card_to_play, card_effect_active):
        '''
        Plays a card in hand, the player chooses which card to play. Card 0 is the first card, card 1 is the second card and so on
        1.Convert card_to_play type from list of strings to list of integers
        2.Then play card
        '''
        cards_to_play = []
        for i in card_to_play:
            #print(i)
            cards_to_play.append(int(i))

        for i in range(len(cards_to_play)):
            self.deck.discard_pile.append(self.player_hand[cards_to_play[i]])

        for i in reversed(cards_to_play):
            #sort the cards to play in the reverse order so when pop is used, it pops the largest to smallest
            self.player_hand.pop(i)
        print("Discard Pile: ")
        print(self.deck.discard_pile)

        if (card_effect_active == True):
            if (self.deck.discard_pile[-1] == "defuse"):
                return Card().defuse(self.deck.discard_pile[-1])
            elif (self.deck.discard_pile[-1] == "future"):
                return Card().future(self.deck.discard_pile[-1],self.deck.deck)
            elif (self.deck.discard_pile[-1] == "shuffle"):
                self.deck.shuffle()
            elif (self.deck.discard_pile[-1] == "skip"):
                return Card().skip()
            elif (self.deck.discard_pile[-1] == "nope"):
                pass
            elif (self.deck.discard_pile[-1] == "attack"):
                return Card().attack()
            elif (self.deck.discard_pile[-1] == "favour"):
                return Card().favour()
            elif (len(cards_to_play) == 3):
                #assuming they are all identical by this stage of the code
                if (self.duplicates(cards_to_play) == True):
                    card_to_steal = raw_input("Which card do you want to steal from the computer? Enter the card name: ")
                return card_to_steal
        return

    def show_cards(self):
        '''Show all cards in hand'''
        print(self.player_hand)
        return self.player_hand

    def show_deck(self):
        '''Shows all cards remaining in deck'''
        print(self.deck.show_deck())
        return

    def show_discard_pile(self):
        '''Shows cards in the discard pile'''
        #print self.deck.discard_pile
        print(self.deck.discard_pile)
        return self.deck.discard_pile


    def player_turn(self,skip):
        '''Skips the next player's turn'''
        if (skip == True):
            print("False")
            return False
        return True

    def search_defuse(self):
        '''Looks for a defuse card in the hand and finds its position in hand'''
        hand_position = 0
        print(self.player_hand)
        for i in self.player_hand:
            if (i == "defuse"):
                return hand_position
            hand_position += 1
        return

    def duplicates(self,cards_to_play):
        '''Finds idenitcal cards in player's hand'''
        is_duplicate = False
        possible_duplicates = []
        if (self.can_play_duplicates(cards_to_play)):
            if (len(cards_to_play) > 1 and len(cards_to_play) < 4):
                for i in range(len(cards_to_play)):
                    possible_duplicates.append(self.player_hand[int(cards_to_play[i])])
                if (len(set(possible_duplicates)) == 1):
                    print("True1")
                    is_duplicate = True
                else:
                    print("False1")
                    is_duplicate = False
            return is_duplicate
        return False

    def can_play_duplicates(self,cards_to_play):
        '''
        Checks the cards played for duplicates are valid cards.
        Eg, only non-special cards can be played, attack card has speial affect so it cannot be used as duplicates
        '''
        good_cards = ['taco','beard','water_mallon','hairy_potatoe','rainbow']
        if (self.player_hand[int(cards_to_play[0])] in good_cards):
            return True
        return False

    def pick_card_to_give(self):
        '''Pick a car you want to give to your opponent'''
        #Check that card_to_give has only 1 item
        card_to_give = raw_input("Which card do you want to give away? Enter the number: ")
        card_to_give = self.player_hand.pop(int(card_to_give))
        #adds the item to computer's hand
        return card_to_give

    def nope_logic(self):
        '''
        Player Nope:
            If player has nope card in hand ask if nope wants to be played after the computer has played a card
        '''
        to_play = raw_input("Do you want to play your Nope card? Y/N: ")
        if (to_play == "Y" or to_play == "y"):
            card_effect_active = True
            self.player_hand.remove("nope")
            self.deck.discard_pile.append("nope")
        else:
            card_effect_active = False
        return card_effect_active

class Computer(Player):
    '''
    Creates the computer hand and actions associated with the computer
    '''
    def __init__(self, deck):
        '''Computer object still needs to access the same deck as the players'''
        self.player_hand = ["defuse"]
        self.deck = deck
        for i in range(6):
            self.draw_card()

    def draw_card(self):
        #draw pile reduces by one
        self.player_hand.append(self.deck.pickup())
        return self.player_hand


    def play_card(self, card_to_play, card_effect_active):
        '''
        #Computer AI plays a card based on card_played by player
        #decides to draw or play card
        #keeps drawing card until there are only 16 cards Left
        #if Computer has no diffuse use 3 cards to get a defuse card from player
        #use future if there are 20cards or less
        #draw card
        #plays defuse if drawn exploding kittens

        For now just plays the second card in hand. Computer play logic to be developed
        '''
        return super(Computer, self).play_card(card_to_play, card_effect_active)

    def play_logic(self):
        """
        1. If less than 35 cards remaining in deck and have future card play once every 3 returns
        #2. Don't play cards until there are only 25 cards left
        3. If future[0] to future[2] is exploding kitten and have shuffle and has more than 14 cards in deck
           #Play shuffle
           #Else play skip
           Else play double to steal cards before drawing
        #4. Put exlpoding kitten on the 5th if exploding kitten is drawn
        5. Play nope if opponent plays double or tripple to card_to_steal
        6. If deck has less than 10 cards start to steal cards by using favour or double
        7. Only use tripple if you have to steal defuse and you have to draw a card afterwards and there is defuse in opponent hands

        Output is card to play so it must be a number in string
        need to link to play_pattern()
        """
        if (self.deck.deck_size < 25):
            if (self.deck.deck_size <=10 and "favour" in self.player_hand):
                cards_to_play = str(self.player_hand.index("favour"))
                return cards_to_play
            cards_to_play = play_skip_or_attack()
            if (self.deck.deck_size < 35 and self.deck.deck_size > 10 and "future" in self.player_hand):
                self.player_hand.remove("future")
                self.deck.discard_pile.append("future")
                #add play once every 3 turn
                if (True in list(map(search_exploding_kitten,deck[:3]))):
                    if ("shuffle" in self.player_hand and self.deck.deck_size > 14):
                        cards_to_play = str(self.player_hand.index("shuffle")) #return the string format of a number representing the location of the the card in hand
                        return cards_to_play
                    elif ("skip" in self.player_hand):
                        cards_to_play = str(self.player_hand.index("skip"))
                        return cards_to_play
                    else:
                        cards_to_play = str(self.player_hand.index("favour"))
                        return cards_to_play
            elif (self.deck.deck_size < 35 and self.deck.deck_size > 10 and "future" not in self.player_hand):
                cards_to_play = play_skip_or_attack()

        if ("exploding_kitten" in self.player_hand and "defuse" in self.player_hand):
            self.deck.inset(4,"exploding_kitten") #puts the exploding kitten card back in the deck (5th card)

        return

    def play_skip_or_attack(self):
        '''
        plays skip or attack in emergency situations
        '''
        if (self.deck.deck_size <=10 and "skip" in self.player_hand):
            cards_to_play = str(self.player_hand.index("skip"))
        if (self.deck.deck_size <=10 and "attack" in self.player_hand):
            cards_to_play = str(self.player_hand.index("attack"))
        return cards_to_play

    def nope_logic(self,opponent_play):
        '''
        Computer Nope:
            If computer has nope in hand:
                If opponent plays defuse play nope
                If opponent plays attack or skips
        '''
        #Computer doesn't play nope when defuse is played automatically when the exploding kitten is drawn
        #It only works when player selects the defuse card during play, need to fix this
        card_effect_active = True
        if ("nope" in self.player_hand):
            if (opponent_play == "defuse" or opponent_play == "attack" or opponent_play == "skip"):
                card_effect_active = False
                self.player_hand.remove("nope") #Removes the nope card from hand
                self.deck.discard_pile.append("nope") #Adds the nope card to the discard pile
        return card_effect_active

    def favour_logic(self):
        '''
        Gives away taco, beard, rainbow, water_mallon first when player asks for a card.
        If computer doens't have them then give away shuffle then skip.
        This assumes the computer will always have at least one of those cards which is highly probable
        given the number of those cards in the deck.
        '''

        cards_to_give_type_one = ["taco", "beard", "rainbow", "water_mallon"]
        type_one = [card for card in self.player_hand if card in cards_to_give_type_one]
        type_one = list(set(type_one))
        cards_to_give_type_two = ["shuffle", "skip"]
        type_two = [card for card in self.player_hand if card in cards_to_give_type_two]
        type_two = list(set(type_two))
        if (not type_one):
            card_to_give = type_two[0]
        else:
            card_to_give = type_one[0]
        return card_to_give

    def show_cards(self):
        '''show all cards in hand'''
        print(self.player_hand)
        return self.player_hand

    def search_exploding_kitten(self,top_three_cards):
        return top_three_cards == "exploding_kitten"

#Common functions used outside of classes
def common_tasks(whos_turn, next_person):
    '''Asks for which card or cards to play and put them in a list where there is a space between them from the input
    returns a string representation of a number, which is the card location in hand
    '''
    print(whos_turn is player)
    print(whos_turn is computer)
    if (whos_turn is player):
        cards_to_play = raw_input("Which card or cards do you want to play? Enter the number: ")
    else:
        cards_to_play = computer.play_logic()#"1" #Replace with computer.play_logic()
    if (cards_to_play != None):
        cards_to_play = cards_to_play.split()
    #print(cards_to_play)
        if (len(cards_to_play) > 1 and len(cards_to_play) < 4):
            if (whos_turn.duplicates(cards_to_play) == True and len(cards_to_play) == 2):
                #otherwise the computer asks for a card. For now let it always be the zeroth cards
                card_to_steal = "0"
                if (whos_turn is player):
                    card_to_steal = raw_input("Which card do you want to steal? Enter the number: ")
                stolen_card = next_person.player_hand.pop(int(card_to_steal))
                print("Stole card: %s" % stolen_card)
                whos_turn.player_hand.append(stolen_card)
            elif (whos_turn.duplicates(cards_to_play) == True and len(cards_to_play) == 3):
                #otherwise the computer asks for a card. For now let it always be defuse all the time
                card_to_steal = "defuse"
                if (whos_turn is player):
                    card_to_steal = raw_input("What card do you want to steal? Enter the card name: ")
                if (card_to_steal in next_person.player_hand):
                    whos_turn.player_hand.append(card_to_steal)
                else:
                    print("The card picked is not in the opponent's hand")
            else:
                print("Cards played are not valid")
                cards_to_play = common_tasks(whos_turn, next_person)
    return cards_to_play

def check_kitten_explodes():
    '''Checks if the exploding kitten is in the player's hands'''
    if ("exploding_kitten" in player.player_hand or "exploding_kitten" in computer.player_hand):
        return True
    return False

def play_pattern(whos_turn,next_person):
    '''Play pattern of the game'''
    kitten_explodes = False
    card_drawn = False
    cards_to_play = common_tasks(whos_turn,next_person)
    card_effect = "None"
    card_effect_active = True
    if cards_to_play != None:
        if (whos_turn is player):
            card_effect_active = next_person.nope_logic(whos_turn.player_hand[map(int,cards_to_play)[0]]) #nope logic for computer
            card_effect = player.play_card(cards_to_play, card_effect_active)
        else:
            card_effect_active = next_person.nope_logic() #nope logic for player
            card_effect = computer.play_card(cards_to_play, card_effect_active)

    if (game_deck.discard_pile[-1] != "skip"):
        #if (player.skip() !=):
        if (card_effect == "favour"):
            if (whos_turn is computer):
                whos_turn.player_hand.append(player.pick_card_to_give())
            else:
                whos_turn.player_hand.append(computer.favour_logic())
        if (card_effect == "attack"):
            whos_turn.draw_card()
            kitten_explodes = check_kitten_explodes()
            for i in range(2):
                play_pattern(next_person,whos_turn)
                kitten_explodes = check_kitten_explodes()
                if (game_deck.discard_pile[-1] != "skip"):
                    next_person.draw_card() #player.draw_card()
                if (i == 1):
                    if (whos_turn is player):
                        whos_turn = computer
                        next_person = player
                    else:
                        whos_turn = player
                        next_person = computer
        else:
            whos_turn.draw_card()
            card_drawn = True
    else:
        print("skip card played")

    if cards_to_play == None and card_drawn == False:
        whos_turn.draw_card()

    kitten_explodes = check_kitten_explodes()
    if (kitten_explodes == True):
        if (whos_turn.search_defuse() != None):
            whos_turn.play_card([whos_turn.search_defuse()], card_effect_active) #Only works for player not AI at this stage
            game_deck.deck.append("exploding_kitten") #Puts the exploding kittten back in the bottom of the deck
            del whos_turn.player_hand[-1] #removes the exploding kitten from the player's hand
            kitten_explodes = False #Kitten no longer explodes

    sys.stdout.write(RED)
    print("Computer Hand: ")
    computer.show_cards()
    sys.stdout.write(BLUE)
    print("Player Hand: ")
    player.show_cards()
    sys.stdout.write(GREEN)
    print("Game Deck: %s" % game_deck.show_deck())
    sys.stdout.write(RESET)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    return whos_turn, next_person, kitten_explodes

#Creats deck, player and computer hand
if __name__ == "__main__":
    game_deck = Deck()
    computer = Computer(game_deck)
    sys.stdout.write(RED)
    print("Computer Hand: ")
    computer.show_cards()
    player = Player(game_deck)
    sys.stdout.write(BLUE)
    print("Player Hand: ")
    player.show_cards()
    game_deck.add_exploding_kittens()
    game_deck.shuffle()
    sys.stdout.write(GREEN)
    print("Game Deck: %s" % game_deck.show_deck())
    print("Number of cards remaining in deck: %d" %game_deck.deck_size())
    sys.stdout.write(RESET)
    #When the game starts player makes the first move
    whos_turn = player
    next_person = computer
    kitten_explodes = False
    #Keeps playing until someone gets the exploding kitten
    while kitten_explodes == False:
        whos_turn, next_person, kitten_explodes = play_pattern(whos_turn,next_person)

        if (whos_turn is player):
            whos_turn = computer
            next_person = player
        else:
            whos_turn = player
            next_person = computer
    print("GAME OVER")
    #machine = Computer()
