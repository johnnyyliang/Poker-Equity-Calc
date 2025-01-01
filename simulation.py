from cardclass import Card
from deckclass import Deck
from handclass import Hand
import numpy as np

class Simulator(object):
    def __init__(self, num_sim = 10000):
        self.sims = num_sim

    def run_sim(self):
        holeself1_suit = str(input('Input a Suit for Self Hole Card 1: '))
        holeself1_val = str(input('Input a Value for Self Hole Card 1: '))
        holeself2_suit = str(input('Input a Suit for Self Hole Card 2: '))
        holeself2_val = str(input('Input a Value for Self Hole Card 2: '))

        holeother1_suit = str(input('Input a Suit for Other Hole Card 1: '))
        holeother1_val = str(input('Input a Value for Other Hole Card 1: '))
        holeother2_suit = str(input('Input a Suit for Other Hole Card 2: '))
        holeother2_val = str(input('Input a Value for Other Hole Card 2: '))

        selfhand = Hand([Card(holeself1_val, holeself1_suit), Card(holeself2_val, holeself2_suit)])
        otherhand = Hand([Card(holeother1_val, holeother1_suit), Card(holeother2_val, holeother2_suit)])


        wins_self = 0
        wins_other = 0
        ties = 0
        for i in range(self.sims):

            for card in selfhand.hand:
                Deck.DECK.remove(card)
            for card in otherhand.hand:
                Deck.DECK.remove(card)

            community_cards = Deck.deal(5)
            copyself = Hand(selfhand.hand[:])
            copyother = Hand(otherhand.hand[:])
            copyself.hand += community_cards
            copyother.hand += community_cards
            winner = copyself.compare(copyother)
            Deck.reset()

            if 'Self wins' in winner:
                wins_self += 1
            elif 'Other wins' in winner:
                wins_other += 1
            else:
                ties += 1
        
        print(f'Self wins {100 * wins_self/self.sims}%, Other wins {100 * wins_other/self.sims}%, Tie {100 * ties/self.sims}%')
        
if __name__ == '__main__':
    simulation = Simulator()
    results = simulation.run_sim()