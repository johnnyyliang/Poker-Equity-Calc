from deckclass import Deck
from cardclass import Card

class Hand(object):
    """
    A class representing a hand of cards in poker.
    Provides methods to evaluate and rank the hand according to poker rules.
    """

    def __init__(self, cards):
        """
        Initializes the hand.

        Parameter cards: The cards in the hand.
        Precondition: cards is a list of card objects.
        """
        for card in cards:
            assert isinstance(card, Card)

        self.hand = cards
        self.evaluation = 'High Card'


    def __getitem__(self, index):
        """
        Retrieves the card at the specified index in the hand.

        Parameter index: The position of the card to retrieve.
        Precondition: index is an integer within the range of the hand.
        """
        assert isinstance(index, int)

        return self.hand[index]
    

    def __len__(self):
        """
        Returns an integer representing the size of the hand.
        """
        return len(self.hand)
    
    def __repr__(self):
        s = ''
        for card in self.hand:
            s += repr(card)
        return repr(self.hand[0]) + ' and ' + repr(self.hand[1])
    

    def sort_value(self):
        """
        Sorts the cards in the hand by their rank values in ascending order.
        """
        for i in range(len(self.hand) - 1):
            for j in range(len(self.hand) - 1):
                if self.hand[j] > self.hand[j + 1]:
                    tmp = self.hand[j]
                    self.hand[j] = self.hand[j + 1]
                    self.hand[j + 1] = tmp


    def high_card(self):
        """
        Determines the high card in the hand.
        """
        self.evaluation = 'High Card'

    def flush(self):
        """
        Determines if the hand is a flush.
        """
        spade_accum = 0
        heart_accum = 0 
        club_accum = 0
        diamond_accum = 0

        for card in self.hand:
            if card.getSuit() == 'S':
                spade_accum += 1
            elif card.getSuit() == 'H':
                heart_accum += 1
            elif card.getSuit() == 'C':
                club_accum += 1
            elif card.getSuit() == 'D':
                diamond_accum += 1

        accum_list = [spade_accum, heart_accum, club_accum, diamond_accum]
        for accum in accum_list:
            if accum >= 5:
                self.evaluation = 'Flush'
            else:
                pass
        

    def straight(self):
        """
        Determines if the hand is a straight.
        """
        self.sort_value()

        straight_cards_self = set()
        selfbest = 0
        for card in self.hand:
            straight_cards_self.add(card.getValue())

        for i in range(2, 10):
            if {i, i+1, i+2, i+3, i+4}.issubset(straight_cards_self):
                self.evaluation = 'Straight'

        
        values = set()
        for card in self.hand:
            values.add(card.getValue())

        ace_low_straight = {14, 2, 3, 4, 5}
        if ace_low_straight.issubset(values):
            self.evaluation = 'Straight'

        
    def trips(self):
        """
        Determines if the hand contains three cards of the same rank (trips).
        """
        rank_count = {}

        for card in self.hand:
            rank = card.getRank()
            if rank in rank_count:
                rank_count[rank] += 1
            else:
                rank_count[rank] = 1

        trips = 0
        for count in rank_count.values():
            if count == 3:
                trips += 1

        if trips >= 1:
            self.evaluation = 'Trips'
        

    def pair(self):
        """
        Determines if the hand contains a pair.
        """
        rank_count = {}

        for card in self.hand:
            rank = card.getRank()
            if rank in rank_count:
                rank_count[rank] += 1
            else:
                rank_count[rank] = 1

        pairs = 0
        for count in rank_count.values():
            if count == 2:
                pairs += 1

        if pairs >= 1:
            self.evaluation = 'Pair'

    def two_pair(self):
        """
        Determines if the hand contains two pairs.
        """
        rank_count = {}

        for card in self.hand:
            rank = card.getRank()
            if rank in rank_count:
                rank_count[rank] += 1
            else:
                rank_count[rank] = 1

        pairs = 0
        for count in rank_count.values():
            if count == 2:
                pairs += 1

        if pairs >= 2:
            self.evaluation = 'Two Pair'

    def royal_flush(self):
        """
        Determines if the hand is a royal flush.
        """
        spade_accum = []
        heart_accum = []
        club_accum = []
        diamond_accum = []

        for card in self.hand:
            if card.getSuit() == 'S':
                spade_accum.append(card)
            elif card.getSuit() == 'H':
                heart_accum.append(card)
            elif card.getSuit() == 'C':
                club_accum.append(card)
            elif card.getSuit() == 'D':
                diamond_accum.append(card)

        accum_list = [spade_accum, heart_accum, club_accum, diamond_accum]
        for accum in accum_list:
            if len(accum) >= 5:
                hand = Hand(accum)
                for card in hand.hand:
                    if card.getValue() < 10:
                        hand.hand.remove(card)
                hand.straight()
                if hand.evaluation == 'Straight':
                    hand.flush()
                    if hand.evaluation == 'Flush':
                        self.evaluation = 'Royal Flush'



    def straight_flush(self):
        """
        Determines if the hand is a straight flush.
        """
        spade_accum = []
        heart_accum = []
        club_accum = []
        diamond_accum = []

        for card in self.hand:
            if card.getSuit() == 'S':
                spade_accum.append(card)
            elif card.getSuit() == 'H':
                heart_accum.append(card)
            elif card.getSuit() == 'C':
                club_accum.append(card)
            elif card.getSuit() == 'D':
                diamond_accum.append(card)

        accum_list = [spade_accum, heart_accum, club_accum, diamond_accum]
        for accum in accum_list:
            if len(accum) >= 5:
                hand = Hand(accum)
                hand.straight()
                if hand.evaluation == 'Straight':
                    self.evaluation = 'Straight Flush'


    def quads(self):
        """
        Determines if the hand contains four cards of the same rank (quads).
        """
        rank_count = {}

        for card in self.hand:
            rank = card.getRank()
            if rank in rank_count:
                rank_count[rank] += 1
            else:
                rank_count[rank] = 1

        quads = 0
        for value in rank_count.values():
            if value == 4:
                quads += 1
        
        if quads == 1:
            self.evaluation = 'Quads'


    def full_house(self):
        """
        Determines if the hand is a full house.
        """
        rank_count = {}

        for card in self.hand:
            rank = card.getRank()
            if rank in rank_count:
                rank_count[rank] += 1
            else:
                rank_count[rank] = 1

        pairs = 0
        trips = 0
        for count in rank_count.values():
            if count == 2:
                pairs += 1
            if count == 3:
                trips += 1

        if (pairs >= 1 and trips >= 1) or (trips >= 2):
            self.evaluation = 'Full House'


    def rank(self):
        """
        Evaluates and returns rank of the hand based on poker rules, updating the eval attribute.
        """
        self.high_card()
        self.pair()
        self.two_pair()
        self.trips()
        self.straight()
        self.flush()
        self.full_house()
        self.quads()
        self.straight_flush()
        self.royal_flush()
        return self.evaluation
    

    def high_card_compare(self, other):
        """
        Helper function for compare
        """
        selfvals = []
        for card in self.hand:
            selfvals.append(card.getValue())
        selfvals.sort()
        selfvals = selfvals[-5:]
        othervals = []
        for card in other.hand:
            othervals.append(card.getValue())
        othervals.sort()
        othervals = othervals[-5:]

        self_max = 0
        other_max = 0
        i = 0
        while i < 5:
            if self_max != other_max:
                break
            self_max = max(selfvals)
            other_max = max(othervals)
            selfvals = selfvals[:-1]
            othervals = othervals[:-1]
            i += 1

        if self_max > other_max:
            return 'Self wins'
        elif self_max < other_max:
            return 'Other wins'
        else:
            return 'Tie'


    def pair_compare(self, other):
        selfpairs = {}
        otherpairs = {}

        for card in self.hand:
            val = card.getRank()
            accum = 0
            for i in range(len(self.hand)):
                if self.hand[i].getRank() == val:
                    accum += 1
            if accum == 2:
                selfpairs[card.getValue()] = 'Pair'

        for card in other.hand:
            val = card.getRank()
            accum = 0
            for i in range(len(other.hand)):
                if other.hand[i].getRank() == val:
                    accum += 1
            if accum == 2:
                otherpairs[card.getValue()] = 'Pair'
        
        if max(selfpairs) > max(otherpairs):
            return 'Self wins'
        elif max(selfpairs) < max(otherpairs):
            return 'Other wins'
        else:
            selfnonpair = []
            othernonpair = []
            for card in self.hand:
                if not card.getValue() in selfpairs:
                    selfnonpair.append(card.getValue())
            for card in other.hand:
                if not card.getValue() in otherpairs:
                    othernonpair.append(card.getValue())
            selfnonpair.sort(reverse = True)
            othernonpair.sort(reverse = True)
            selfnonpair = selfnonpair[:3]
            othernonpair = othernonpair[:3]
            for i in range(3):
                if selfnonpair[0] > othernonpair[0]:
                    return 'Self wins'
                elif selfnonpair[0] < othernonpair[0]:
                    return 'Other wins'
                elif i == 2:
                    return 'Tie'
                elif selfnonpair[0] == othernonpair[0]:
                    selfnonpair = selfnonpair[1:]
                    othernonpair = othernonpair[1:]


    def two_pair_compare(self, other):
        selfpairs = {}
        otherpairs = {}

        for card in self.hand:
            val = card.getRank()
            accum = 0
            for i in range(len(self.hand)):
                if self.hand[i].getRank() == val:
                    accum += 1
            if accum == 2:
                selfpairs[card.getValue()] = 'Pair'

        for card in other.hand:
            val = card.getRank()
            accum = 0
            for i in range(len(other.hand)):
                if other.hand[i].getRank() == val:
                    accum += 1
            if accum == 2:
                otherpairs[card.getValue()] = 'Pair'
        
        if len(selfpairs) > 2:
            del selfpairs[min(selfpairs)]
        if len(otherpairs) > 2:
            del otherpairs[min(otherpairs)]

        if max(selfpairs) > max(otherpairs):
            return 'Self wins'
        elif max(selfpairs) < max(otherpairs):
            return 'Other wins'
        
        elif max(selfpairs) == max(otherpairs):
            if min(selfpairs) > min(otherpairs):
                return 'Self wins'
            elif min(selfpairs) < min(otherpairs):
                return 'Other wins'
            elif min(selfpairs) == min(otherpairs):
                selfnonpair = []
                othernonpair = []

                for card in self.hand:
                    if not card.getValue() in selfpairs:
                        selfnonpair.append(card.getValue())
                for card in other.hand:
                    if not card.getValue() in otherpairs:
                        othernonpair.append(card.getValue())
                if max(selfnonpair) > max(othernonpair):
                    return 'Self wins'
                elif max(selfnonpair) < max(othernonpair):
                    return 'Other wins'
                elif max(selfnonpair) == max(othernonpair):
                    return 'Tie'



    def trips_compare(self,other):
        """
        Returns winner if both hands have trips

        Precondition: other is an instance of Hand
        """
        assert isinstance(other, Hand)

        selftrips = {}
        othertrips = {}

        for card in self.hand:
            val = card.getRank()
            accum = 0
            for i in range(len(self.hand)):
                if self.hand[i].getRank() == val:
                    accum += 1
            if accum == 3:
                selftrips[card.getValue()] = 'Trips'

        for card in other.hand:
            val = card.getRank()
            accum = 0
            for i in range(len(other.hand)):
                if other.hand[i].getRank() == val:
                    accum += 1
            if accum == 3:
                othertrips[card.getValue()] = 'Trips'

        if max(selftrips) > max(othertrips):
            return 'Self wins'
        elif max(selftrips) < max(othertrips):
            return 'Other wins'
        else:
            selfnontrips = []
            othernontrips = []
            for card in self.hand:
                if not card.getValue() in selftrips:
                    selfnontrips.append(card.getValue())
            for card in other.hand:
                if not card.getValue() in othertrips:
                    othernontrips.append(card.getValue())
            selfnontrips.sort(reverse = True)
            othernontrips.sort(reverse = True)
            selfnontrips = selfnontrips[:2]
            othernontrips = othernontrips[:2]
            for i in range(2):
                if selfnontrips[0] > othernontrips[0]:
                    return 'Self wins'
                elif selfnontrips[0] < othernontrips[0]:
                    return 'Other wins'
                elif i == 1:
                    return 'Tie'
                elif selfnontrips[0] == othernontrips[0]:
                    selfnontrips = selfnontrips[1:]
                    othernontrips = othernontrips[1:]


    def straight_compare(self, other, straight_flush = False):
        """
        Returns winner if both hands have a straight

        Precondition: other is an instance of Hand
        """
        self.sort_value()
        other.sort_value()

        straight_cards_self = set()
        selfbest = 0
        for card in self.hand:
            straight_cards_self.add(card.getValue())
        
        straight_cards_other = set()
        otherbest = 0
        for card in other.hand:
            straight_cards_other.add(card.getValue())

        for i in range(2, 10):
            if {i, i+1, i+2, i+3, i+4}.issubset(straight_cards_self):
                selfbest = i + 4

        for i in range(2, 10):
            if {i, i+1, i+2, i+3, i+4}.issubset(straight_cards_other):
                otherbest = i + 4


        if straight_flush:
            if selfbest > otherbest:
                return 'Self wins'
            elif selfbest < otherbest:
                return 'Other wins'
            else:
                return 'Tie'
            
        elif not straight_flush:
            if selfbest > otherbest:
                return 'Self wins'
            elif selfbest < otherbest:
                return 'Other wins'
            else:
                return 'Tie'


    def flush_compare(self, other):
        spades_self = []
        hearts_self = []
        clubs_self = []
        diamonds_self = []

        for card in self.hand:
            if card.getSuit() == 'S':
                spades_self.append(card)
            elif card.getSuit() == 'H':
                hearts_self.append(card)
            elif card.getSuit() == 'C':
                clubs_self.append(card)
            elif card.getSuit() == 'D':
                diamonds_self.append(card)

        accums_self = [spades_self, hearts_self, clubs_self, diamonds_self]
        flush_suit = None
        flush_self = []
        for accum in accums_self:
            if len(accum) >= 5:
                flush_suit = accum[0].getSuit()
                for card in accum:
                    flush_self.append(card)

        flush_other = []

        for card in other.hand:
            if card.getSuit() == flush_suit:
                flush_other.append(card)

        flush_other.sort()
        flush_self.sort()
        flush_other = flush_other[-5:]
        flush_self = flush_self[-5:]

        if max(flush_self) > max(flush_other):
            return 'Self wins'
        else:
            return 'Other wins'


    def full_house_compare(self, other):
        selftrips = {}
        othertrips = {}

        for card in self.hand:
            val = card.getRank()
            accum = 0
            for i in range(len(self.hand)):
                if self.hand[i].getRank() == val:
                    accum += 1
            if accum == 3:
                selftrips[card.getValue()] = 'Trips'

        for card in other.hand:
            val = card.getRank()
            accum = 0
            for i in range(len(other.hand)):
                if other.hand[i].getRank() == val:
                    accum += 1
            if accum == 3:
                othertrips[card.getValue()] = 'Trips'

        selfpairs = {}
        otherpairs = {}

        for card in self.hand:
            val = card.getRank()
            accum = 0
            for i in range(len(self.hand)):
                if self.hand[i].getRank() == val:
                    accum += 1
            if accum == 2:
                selfpairs[card.getValue()] = 'Pair'

        for card in other.hand:
            val = card.getRank()
            accum = 0
            for i in range(len(other.hand)):
                if other.hand[i].getRank() == val:
                    accum += 1
            if accum == 2:
                otherpairs[card.getValue()] = 'Pair'

        if max(selftrips) > max(othertrips):
            return 'Self wins'
        elif max(selftrips) < max(othertrips):
            return 'Other wins'
        if len(selftrips) > 1 and len(othertrips) > 1:
            if min(selftrips) > min(othertrips):
                return 'Self wins'
            elif min(selftrips) < min(othertrips):
                return 'Other wins'
            elif min(selftrips) == min(othertrips):
                return 'Tie'
        elif len(selftrips) > 1:
            if min(selftrips) > max(otherpairs):
                return 'Self wins'
            elif min(selftrips) < max(otherpairs):
                return 'Other wins'
            elif min(selftrips) == max(otherpairs):
                return 'Tie'
        elif len(othertrips) > 1:
            if max(selfpairs) > min(othertrips):
                return 'Self wins'
            elif max(selfpairs) < min(othertrips):
                return 'Other wins'
            elif max(selfpairs) == min(othertrips):
                return 'Tie'
        if max(selfpairs) > max(otherpairs):
            return 'Self wins'
        elif max(selfpairs) < max(otherpairs):
            return 'Other wins'
        else:
            return 'Tie'


    def quads_compare(self, other):
        selfquads = {}
        otherquads = {}

        for card in self.hand:
            val = card.getRank()
            accum = 0
            for i in range(len(self.hand)):
                if self.hand[i].getRank() == val:
                    accum += 1
            if accum == 4:
                selfquads[card.getValue()] = 'Quads'

        for card in other.hand:
            val = card.getRank()
            accum = 0
            for i in range(len(other.hand)):
                if other.hand[i].getRank() == val:
                    accum += 1
            if accum == 4:
                otherquads[card.getValue()] = 'Quads'
        if max(selfquads) > max(otherquads):
            return 'Self wins'
        elif max(selfquads) < max(otherquads):
            return 'Other wins'
        else:
            selfnonquads = []
            othernonquads = []
            for card in self.hand:
                if not card.getValue() in selfquads:
                    selfnonquads.append(card.getValue())
            for card in other.hand:
                if not card.getValue() in otherquads:
                    othernonquads.append(card.getValue())
            if max(selfnonquads) > max(othernonquads): 
                return 'Self wins'
            elif max(selfnonquads) < max(othernonquads):
                return 'Other wins'
            else:
                return 'Tie'



    def straight_flush_compare(self, other):
        return self.straight_compare(other, straight_flush = True)


    def royal_flush_compare(self, other):
        return 'Tie'


    def equal_ranks(self, other):
        if self.evaluation == 'High Card':
            return self.high_card_compare(other)
        elif self.evaluation == 'Pair':
            return self.pair_compare(other)
        elif self.evaluation == 'Two Pair':
            return self.two_pair_compare(other)
        elif self.evaluation == 'Trips':
            return self.trips_compare(other)
        elif self.evaluation == 'Straight':
            return self.straight_compare(other)
        elif self.evaluation == 'Flush':
            return self.flush_compare(other)
        elif self.evaluation == 'Full House':
            return self.full_house_compare(other)
        elif self.evaluation == 'Quads':
            return self.quads_compare(other)
        elif self.evaluation == 'Straight Flush':
            return self.straight_flush_compare(other)
        elif self.evaluation == 'Royal Flush':
            return self.royal_flush_compare(other)


    def compare(self, other):
        """
        Compares rank of own hand to another

        Precondition: other is an object of class Hand
        """
        assert isinstance(other, Hand)
        self.rank()
        other.rank()

        hand_ranks = {'High Card':1, 'Pair':2, 'Two Pair':3, 'Trips':4, 'Straight':5, 'Flush':6,
                      'Full House':7, 'Quads':8, 'Straight Flush':9, 'Royal Flush':10}
        
        if hand_ranks[self.evaluation] > hand_ranks[other.evaluation]:
            return 'Self wins'
        elif hand_ranks[self.evaluation] < hand_ranks[other.evaluation]:
            return 'Other wins'
        else:
            return self.equal_ranks(other)