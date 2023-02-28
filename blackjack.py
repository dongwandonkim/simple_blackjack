import random

suites = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit
    
class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suites:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one_card(self):
        return self.all_cards.pop()

    def __str__(self):
        return f"Deck of {len(self.all_cards)} cards" 

# new_deck = Deck()
# new_deck.shuffle()
# print(new_deck)
# my_card = new_deck.deal_one_card()
# print(new_deck, my_card)

class Hand:
    def __init__(self,name):
        self.name = name
        self.hand = []

    def hit(self, card):
        self.hand.append(card)
        print(f"{self.name} received {card}")

    def stay(self):
        print("Stay")