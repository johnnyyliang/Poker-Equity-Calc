from cardclass import Card
import random

deck_cards = []
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['H', 'S', 'C', 'D']
for rank in ranks:
    for suit in suits:
        deck_cards.append(Card(rank, suit))


class Deck(object):
    DECK = deck_cards

    def __init__(self):
        pass
    
    def deal(n):
        random.shuffle(Deck.DECK)
        to_deal = []
        for i in range(n):
            tbd = Deck.DECK[0]
            del Deck.DECK[0]
            to_deal.append(tbd)
        return to_deal
    

    def reset():
        deck = []
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['H', 'S', 'C', 'D']
        for rank in ranks:
            for suit in suits:
                deck.append(Card(rank, suit))
        Deck.DECK = deck