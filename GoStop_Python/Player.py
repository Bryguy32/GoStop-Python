##############################################################
# Name:  Bryan Francis
# Project : GoStop Python
# Class : OPL Spring 2020
# Date : 3/27/2020
##############################################################
from Deck import Deck

class Player(object):

##############################################################
# Function Name: Constructor
# Purpose: Constructor
# Parameters: 
#           self, int score
# Assistance Received: None
##############################################################
    def __init__(self, score = 0):
        self.score = score
        self.isTurn = False
        self.tripCapPos = [0, 0, 0]
        self.cardPosition = 0

##############################################################
# Function Name: setScore
# Purpose: sets the score
# Parameters: 
#           self, int score
# Assistance Received: None
##############################################################
    def setScore(self, score):

        self.score = score

##############################################################
# Function Name: getScore
# Purpose: returns the score
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def getScore(self):

        return self.score

##############################################################
# Function Name: setTurn
# Purpose: sets the turn
# Parameters: 
#           self, bool turn
# Assistance Received: None
##############################################################
    def setTurn(self, turn):

        self.isTurn = turn

##############################################################
# Function Name: getIsTurn
# Purpose: returns the turn
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def getIsTurn(self):

        return self.isTurn

##############################################################
# Function Name: getTripCapPos
# Purpose: returns triple cap positions
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def getTripCapPos(self):

        return self.tripCapPos

##############################################################
# Function Name: getCardPosition
# Purpose: returns the card position
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def getCardPosition(self):

        return self.cardPosition

##############################################################
# Function Name: isStackPair
# Purpose: returns bool if the matching cards in layout are
# a stack pair or two matching cards
# Parameters: 
#           self, layout, cardPosition
# Assistance Received: None
##############################################################
    def isStackPair(self, layout, cardPosition):

        if (cardPosition == 0):

            return False

        elif (cardPosition + 1 >= len(layout)):

            return False

        elif (layout[cardPosition -1].cardMatcher() == "["):

            return True

        elif (layout[cardPosition + 1].cardMatcher() == "]"):

            return True

        #/* Check to make sure not triple cap as well */
        elif (layout[cardPosition - 1].getFace() == layout[cardPosition].getFace() and
		    layout[cardPosition + 1].getFace() == layout[cardPosition].getFace()):

		#/* make sure cardPosition is not out of range */
            if (cardPosition - 2 >= 0 and layout[cardPosition - 2].cardMatcher() == "["):

                return True


        return False;

##############################################################
# Function Name: stackPairMatchesStockPile
# Purpose: checks if a layout card matches the first stockPile card
# Parameters: 
#           self, layout, stockPile
# Assistance Received: None
##############################################################
    def stackPairMatchesStockPile(self, layout, stockPile):

        for l in layout:

            if( l.getFace() == stockPile[0].getFace()):
                
                return True

        return False

##############################################################
# Function Name: tripleCapPositions
# Purpose: looks for tripleCap then copies positions of tripleCap
# Parameters: 
#           self, layout, choosenCard
# Assistance Received: None
##############################################################
    def tripleCapPositions(self, layout, choosenCard):           
        
        for i, l in enumerate(layout):
            j = i + 1
            k = j + 1

            if (k + 1 < len(layout) and (i - 1) >= 0):

                if (layout[i - 1].cardMatcher() == "[" and 
                    layout[k + 1].cardMatcher() == "]"):

                    if (l.getFace() == layout[j].getFace() and
                       l.getFace() == layout[k].getFace()):

                        if(choosenCard.getFace() == l.getFace()):
          
                            self.tripCapPos[0] = i
                            self.tripCapPos[1] = j
                            self.tripCapPos[2] = k
                            return True
        
        return False

##############################################################
# Function Name: tripleCap
# Purpose: Checks for a possible triple cap
# Parameters: 
#           self, layout, deck
# Assistance Received: None
##############################################################
    def tripleCap(self, layout, deck):

        count = 0

        for i, x in enumerate(layout):

            for l in layout:

                if (x.getFace() == l.getFace()):

                        count += 1

                if (count == 3):

                    for k, d in enumerate(deck):

                        if (x.getFace() == d.getFace()):

                            self.cardPosition = k
                            return True
            count = 0

        return False

              
                
##############################################################
#Function Name: stackPair
#Purpose: Finds stack pair
#Parameters:
#			self, list<Card> layout, list<Card> deck, 
#			list<Card> capturePile
#			
#Local Variables: None
#Algorithm: (1) Check for stack pair that can be matched with an already captured
#			stackPair to get a point
#			(2) Find a stack pair
#			(3) Get position of card
#
#Assistance Received: none
##############################################################
    def stackPair(self, layout, deck, capturePile):

        count = 0
        self.cardPosition = 0

        for l in layout:

            for i, d in enumerate(deck):

                if (l.getFace() == d.getFace()):

                    self.cardPosition = i

                    for k in capturePile:

                        if (d.getFace() == k.getFace()):
                             
                            count += 1

                    if (count == 2 or count == 6):

                        return True

                count = 0

        if (self.cardPosition != 0):

            return True

        return False

##############################################################
# Function Name: block
# Purpose: Takes a possible stack pair away from enemy
# Parameters: 
#           self, layout, deck, enemyCapturePile
# Assistance Received: None
##############################################################
    def block(self, layout, deck, enemyCapturePile):

        count = 0
        blockCard = 0

        for i, e in enumerate(enemyCapturePile):

            for j, f in enumerate(enemyCapturePile, start = 1):

                if ( e.getFace() == f.getFace()):

                    count += 1

            if (count == 2 or count == 6):

                blockCard = i
                break
            
            count = 0

        if (count == 2 or count == 6):

            for l in layout:

                for j, d in enumerate(deck):

                    if (l.getFace() == enemyCapturePile[blockCard].getFace() and
                        d.getFace() == enemyCapturePile[blockCard].getFace()):

                        self.cardPosition = j
                        return True

        return False

##############################################################
# Function Name: pairFromStockPile
# Purpose: Looks to create a stackPair from stockPile
# Parameters: 
#           self, deck, stockPile
# Assistance Received: None
##############################################################
    def pairFromStockPile(self, deck, stockPile):

        for i, d in enumerate(deck):

            if (stockPile[0].getFace() == d.getFace()):

                self.cardPosition = i
                return True

        return False

##############################################################
# Function Name: play
# Purpose: Human AI help function
# Parameters: 
#           self, stockPile, layout, humanDeck, humanCapture, computerCapture
# Assistance Received: None
##############################################################
    def play(self, stockPile, layout, humanDeck, humanCapture, computerCapture):

        if (self.tripleCap(layout, humanDeck)):

            print("I recommend you play:", humanDeck[self.cardPosition].cardMatcher(), "to capture all four cards")

        elif (self.stackPair(layout, humanDeck, humanCapture)):

            print("I recommend you play:", humanDeck[self.cardPosition].cardMatcher(), "to create a stack pair")

        elif (self.pairFromStockPile(humanDeck, stockPile)):

            print("I recommend you play:", humanDeck[self.cardPosition].cardMatcher(), "to create a stack pair with the stock pile")

        elif (self.block( layout, humanDeck, computerCapture)):

            print("I recommend you play:", humanDeck[self.cardPosition].cardMatcher(), "to block the computer from capturing the cards it needs")

        else:

            print("I don't have any recommendations sorry")

        print()

