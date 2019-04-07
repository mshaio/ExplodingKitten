class Deck:
    def __init__(self):
        self.cards = ["Pot of Greed", "Black Lotus", "Ace of Spades", "Draw Four"]

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

class Computer:
    def __init__(self, difficulty, deck):
        self.difficulty = difficulty
        self.deck = deck

d = Deck()
p = Player("Steve", d)
c = Computer("Easy", d)

#confirm that the player and computer decks are the same object
print(p.deck is c.deck)

#changes made to the deck via p will be observable from c and vice versa
p.deck.cards.append("How to Play Poker Instruction Card")
print(c.deck.cards)
