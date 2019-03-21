import random

class Deck():

    def __init__(self):
    #create the deck
        self.discard_pile = []
        self.deck = self.create_deck()
        self.shuffle()


    def create_deck(self):
        deck = []
        #assign the number of cards for each type to a card (dict)
        deck_stats = {"exploding_kitten":4, "defuse":6, "nope":5, "shuffle":5, "skip":5, "attack":5, "beard":5, "rainbow":5, "taco":5, 'future':5}
        #assign a value to each card for algorithmic purposes

        #create the card by putting the cards into a list then shuffle the list to randomise
        for card in deck_stats.keys():
          for i in range(0,deck_stats[card]):
            deck.append(card)
        return deck

    def shuffle(self):
    #randomise the deck or for when the shuffle card is played
        random.shuffle(self.deck)
        return self.deck

    def pickup(self):
    #picks up the first card on the draw pile
        picked_up = self.deck.pop(0)
        print(picked_up)
        return picked_up

    def deck_size(self):
    #returns the length of the deck
        deck_size = len(self.deck)
        return deck_size

    def get(self):
    #gets the first card on the deck
        print(self.deck[0])
        return self.deck[0]


class Player():

    def __init__(self):
    #create player's initial hand, must have a defuse, get cards from the deck, at the beginning no one can draw an exploding kitten
        pass
        self.player_hand = ["defuse"]
        self.deck = Deck()
        for i in range(6):
            if self.deck.get() != "exploding_kitten":
                self.draw_card()
            elif self.deck.get() == "exploding_kitten":
                self.deck.shuffle()
                i -= 1
                print(i)

    def draw_card(self):
    #draw pile reduces by one
    #deck.create_deck()
    #deck.shuffle()
        self.player_hand.append(self.deck.pickup())
        print(self.deck.deck_size())
        return self.player_hand

    def play_card(self):
    #discard pile increase by one
        self.deck.discard_pile.append(self.player_hand[5])
        print(self.deck.discard_pile)
        return

player = Player()
player.play_card()

#player = Player()


#deck.create_deck()
#deck.shuffle()
#deck.pickup()
