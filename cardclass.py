class Card(object):
    def __init__(self, rank, suit):
        """
        Initializes a card object, with a rank and suit

        Parameter rank: represents the value of the card
        Precondition: rank is an string between [2, 10] or J, Q, K, A

        Parameter suit: the suit of the card
        Precondition: suit is a letter H,S,C,D representing all card suits
        """
        suits = ['H', 'S', 'C', 'D']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        assert suit in suits, repr(suit) + ' is not a valid suit'
        assert rank in ranks, repr(rank) + ' is not a valid rank'

        self._rank = rank
        self._suit = suit


    def getRank(self):
        return self._rank
    
    def getValue(self):
        ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A': 14}
        val = ranks[self.getRank()]
        return val
    
    def getSuit(self):
        return  self._suit
    
    
    def __repr__(self):
        suits = {'H':'Hearts', 'S':'Spades', 'C':'Clubs', 'D':'Diamonds'}
        ranks = {'2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'10', 'J':'Jack', 'Q':'Queen', 'K':'King', 'A': 'Ace'}
        return f'{ranks[self._rank]}' + ' of ' + f'{suits[self._suit]}'
    
    
    def __eq__(self, other):
        """
        Checks for equality of rank, not suit

        Parameter other: some other card being compared to self
        Precondition: other is a card object
        """
        assert isinstance(other, Card)

        if self._rank == other.getRank() and self._suit == other.getSuit():
            return True
        else:
            return False
        
        
    def __lt__(self, other):
        assert isinstance(other, Card)

        ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A': 14}
        if ranks[self._rank] < ranks[other.getRank()]:
            return True
        else:
            return False
        
        
    def __gt__(self, other):
        assert isinstance(other, Card)

        ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A': 14}
        if ranks[self._rank] > ranks[other.getRank()]:
            return True
        else:
            return False
