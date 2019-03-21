import random

class Deck():

    def __init__(self):
        # create the deck
        self.discard_pile = []
        self.deck = self.create_deck()
        self.shuffle()

    def create_deck(self):
        deck = []
        # assign the number of cards for each type to a card (dict)
        deck_stats = {"A": 4, "B": 6, "C": 5, "D": 5, "E": 5, "F": 5, "G": 5, "H": 5, "I": 5, 'J': 5}

        for card in deck_stats.keys():
            for i in range(0, deck_stats[card]):
                deck.append(card)
        return deck

    def shuffle(self):
        # randomise the deck or for when the shuffle card is played
        random.shuffle(self.deck)
        return self.deck

    def pickup(self):
        # picks up the first card on the draw pile
        picked_up = self.deck.pop(0)
        print(picked_up)
        return picked_up


class Player:

    def __init__(self):
        self.player_hand = ["defuse"]
        self.deck = Deck()
        for i in range(6):
            self.draw_card()

    def draw_card(self):
        # draw pile reduces by one
        self.player_hand.append(self.deck.pickup())
        return self.player_hand

player = Player()
