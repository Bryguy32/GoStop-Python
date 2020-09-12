##############################################################
# Name:  Bryan Francis
# Project : GoStop Python
# Class : OPL Spring 2020
# Date : 3/27/2020
##############################################################
from Player import Player
from Deck import Deck
from Card import Card

class Human(Player):

##############################################################
# Function Name: Constructor
# Purpose: Constructor
# Parameters: 
#           self, int score
# Assistance Received: None
##############################################################
    def __init__(self, score = 0):
        self.deck = Deck()
        Player.__init__(self, score = 0)

##############################################################
# Function Name: play
# Purpose: makes a move for the human
# Parameters: 
#           self, int face
# Assistance Received: None
##############################################################
    def play(self, stockPile, layout, humanDeck, humanCapture):
    
        cardMatches = 0
        score = self.getScore()
        isCard = False
        hasCard = False

        while (hasCard == False):

            playCard = input("Please choose a card: ")

            for d in humanDeck:

                if (d.cardMatcher() == playCard.upper()):

                    hasCard = True


        print("The card entered is:", playCard.upper())

        for humanD in humanDeck:

            if (humanD.cardMatcher() == playCard.upper()):

                choosenCard = humanD

                for j, lay in enumerate(layout):

                    if (humanD.getFace() == lay.getFace()):

                        # Check to make sure card is not a stack pair
                        if (self.isStackPair(layout, j) == False):

                            cardMatches += 1
                            isCard = True

                        elif (self.isStackPair(layout, j) == True):
                            
                            isCard = False

                        if (cardMatches == 1 and isCard == True):

                            layoutMatch1 = lay

                        elif (cardMatches == 2 and isCard == True):

                            layoutMatch2 = lay

                        elif (cardMatches == 3 and isCard == True):

                            layoutMatch3 = lay

                break

    

        if (cardMatches == 0 and 
            self.tripleCapPositions(layout, choosenCard) == False):

            layout.append(choosenCard)
            humanDeck.remove(choosenCard)

        elif (cardMatches == 1):

            card =  Card(4, 13)
            layout.append(card)
            layout.append(choosenCard)
            layout.append(layoutMatch1)
            card = Card(4, 14)
            layout.append(card)

            humanDeck.remove(choosenCard)
            layout.remove(layoutMatch1)

        elif (cardMatches == 2):

            print("Card to make a stack pair with:", end = " ")
            layoutMatch1.print()
            layoutMatch2.print()
            print()

            stackCard = ""
            while (True):

                playCard = input("Please choose a card: ")

                if (playCard.upper() == layoutMatch1.cardMatcher()):

                    break

                elif (playCard.upper() == layoutMatch2.cardMatcher()):

                    layoutMatch1 = layoutMatch2
                    break

            card =  Card(4, 13)
            layout.append(card)
            layout.append(choosenCard)
            layout.append(layoutMatch1)
            card = Card(4, 14)
            layout.append(card)

            humanDeck.remove(choosenCard)
            layout.remove(layoutMatch1)

        elif (cardMatches == 3 or 
              self.tripleCapPositions(layout, choosenCard)):

            if (cardMatches == 3):

                humanCapture.append(choosenCard)
                humanCapture.append(layoutMatch1)
                humanCapture.append(layoutMatch2)
                humanCapture.append(layoutMatch3)

                humanDeck.remove(choosenCard)
                layout.remove(layoutMatch3)
                layout.remove(layoutMatch2)
                layout.remove(layoutMatch1)

            else:

                capPos = self.getTripCapPos()

                humanCapture.append(choosenCard)
                humanCapture.append(layout[capPos[0]])
                humanCapture.append(layout[capPos[1]])
                humanCapture.append(layout[capPos[2]])

                humanDeck.remove(choosenCard)

                # Remove triple stack and "[" "]" from layout
                temp = layout[capPos[0] - 1]
                layout.remove(temp)
                layout.remove(layout[capPos[0]])                
                layout.remove(layout[capPos[0]])
                layout.remove(layout[capPos[0]])
                temp = layout[capPos[0] - 1]
                layout.remove(temp)

             
            score += 1

        layoutCardMatches = 0
        isCard = False
        choosenCard = stockPile[0]


        for i, lay in enumerate(layout):

            if (stockPile[0].getFace() == lay.getFace()):

                if (self.isStackPair(layout, i) == False):
                    layoutCardMatches += 1
                    isCard = True

                elif (self.isStackPair(layout, i) == True):

                    isCard = False

                if (layoutCardMatches == 1 and isCard == True):
                    
                    layoutMatch1 = lay

                elif (layoutCardMatches == 2 and isCard == True):

                    layoutMatch2 = lay

                elif (layoutCardMatches == 3 and isCard == True):

                    layoutMatch3 = lay


        if (cardMatches == 0 or cardMatches == 3):

            if (layoutCardMatches == 0 and
                self.tripleCapPositions(layout, choosenCard) == False):

                layout.append(choosenCard)
                stockPile.remove(choosenCard)

            elif (layoutCardMatches == 1):

                humanCapture.append(choosenCard)
                humanCapture.append(layoutMatch1)

                count = 0
                for i in humanCapture:

                    if choosenCard.getFace() == i.getFace():

                        count += 1

                        if (count == 4 or count == 8):

                            score += 1

                stockPile.remove(choosenCard)
                layout.remove(layoutMatch1)

            elif (layoutCardMatches == 2):

                print("Card to make a stack pair with:", end = " ")
                layoutMatch1.print()
                layoutMatch2.print()
                print()

                stackCard = ""
                while (True):

                    playCard = input("Please choose a card: ")

                    if (playCard.upper() == layoutMatch1.cardMatcher()):

                        break

                    elif (playCard.upper() == layoutMatch2.cardMatcher()):

                        layoutMatch1 = layoutMatch2
                        break

                print("THe card entered is:", stackCard)
                
                # Add cards
                humanCapture.append(choosenCard)
                humanCapture.append(layoutMatch1)

                # Score
                count = 0
                for i in humanCapture:

                    if choosenCard.getFace() == humanCapture.getFace():

                        count += 1

                        if (count == 4 or count == 8):

                            score += 1

                # Erase cards
                stockPile.remove(choosenCard)
                layout.remove(layoutMatch1)

            elif (layoutCardMatches == 3 or 
                  self.tripleCapPositions(layout, choosenCard)):

                if (layoutCardMatches == 3):

                    humanCapture.append(choosenCard)
                    humanCapture.append(layoutMatch1)
                    humanCapture.append(layoutMatch2)
                    humanCapture.append(layoutMatch3)

                    # Erase cards
                    stockPile.remove(choosenCard)
                    layout.remove(layoutMatch1)                    
                    layout.remove(layoutMatch2)
                    layout.remove(layoutMatch3)

                else:

                    capPos = self.getTripCapPos()

                    humanCapture.append(choosenCard)
                    humanCapture.append(layout[capPos[0]])
                    humanCapture.append(layout[capPos[1]])
                    humanCapture.append(layout[capPos[2]])

                    stockPile.remove(choosenCard)

                     # Remove triple stack and "[" "]" from layout
                    temp = layout[capPos[0] - 1]
                    layout.remove(temp)
                    layout.remove(layout[capPos[0]])                
                    layout.remove(layout[capPos[0]])
                    layout.remove(layout[capPos[0]])
                    temp = layout[capPos[0] - 1]
                    layout.remove(temp)

                score += 1

        elif (cardMatches == 1 or cardMatches == 2):

            # Doesn't match layout cards or stacked pair or triple stack
            if (layoutCardMatches == 0 and 
                self.stackPairMatchesStockPile(layout, stockPile) == False and 
                self.tripleCapPositions(layout, choosenCard) == False):

                count = len(layout)

                humanCapture.append(layout[count - 2])
                humanCapture.append(layout[count - 3])


                # Score
                scoreCount = 0
                for humanC in humanCapture:

                    if (layout[count - 2].getFace() == humanC.getFace()):

                        scoreCount += 1

                        if (scoreCount == 4 or scoreCount == 8):


                            score += 1

                layout.remove(layout[count - 1])              
                layout.remove(layout[count - 2])
                layout.remove(layout[count - 3])
                layout.remove(layout[count - 4])

                # add card to layout
                layout.append(stockPile[0])
                stockPile.remove(stockPile[0])

            elif (layoutCardMatches == 3 or 
                  self.tripleCapPositions(layout, choosenCard)):

                if (layoutCardMatches == 3):

                    humanCapture.append(choosenCard)
                    humanCapture.append(layoutMatch1)                    
                    humanCapture.append(layoutMatch2)
                    humanCapture.append(layoutMatch3)

                    stockPile.remove(choosenCard)
                    layout.remove(layoutMatch3)
                    layout.remove(layoutMatch2)
                    layout.remove(layoutMatch1)

                else:

                    capPos = self.getTripCapPos()

                    humanCapture.append(choosenCard)
                    humanCapture.append(layout[capPos[0]])
                    humanCapture.append(layout[capPos[1]])
                    humanCapture.append(layout[capPos[2]])

                    stockPile.remove(choosenCard)

                    # Remove triple stack and "[" "]" from layout
                    temp = layout[capPos[0] - 1]
                    layout.remove(temp)
                    layout.remove(layout[capPos[0]])                
                    layout.remove(layout[capPos[0]])
                    layout.remove(layout[capPos[0]])
                    temp = layout[capPos[0] - 1]
                    layout.remove(temp)
                   
                score += 1

                # add stackedCards from H1/H2

                count = len(layout)

                humanCapture.append(layout[count -2])
                humanCapture.append(layout[count - 3])

                # Score

                scoreCount = 0
                for humanC in humanCapture:

                    if (layout[count - 2].getFace() == humanC.getFace()):

                        scoreCount += 1

                        if (scoreCount == 4 or scoreCount == 8):

                            score += 1

                layout.remove(layout[count - 1])               
                layout.remove(layout[count - 2])
                layout.remove(layout[count - 3])
                layout.remove(layout[count - 4])

            elif (layoutCardMatches == 1 or layoutCardMatches == 2):

                # Add cards
                humanCapture.append(choosenCard)
                humanCapture.append(layoutMatch1)

                # Add stacked pair
                count = len(layout)
                humanCapture.append(layout[count - 2])
                humanCapture.append(layout[count - 3])

                # Check for four matching cards from stock pile card
                scoreCount = 0
                for humanCap in humanCapture:
                    if (choosenCard.getFace() == humanCap.getFace()):

                        scoreCount += 1

                        if (scoreCount == 4 or scoreCount == 8):

                            score += 1

                # Check for matching cards from stack pair
                # only if stack pair and stock pile cards are different
                if choosenCard.getFace() != layout[count - 2].getFace():
                    scoreCount = 0
                    for humanC in humanCapture:

                        if (layout[count - 2].getFace() == humanC.getFace()):

                            scoreCount += 1

                            if (scoreCount == 4 or scoreCount == 8):

                                score += 1

                # Remove cards
                stockPile.remove(choosenCard)
                layout.remove(layoutMatch1)

                count = len(layout)
                layout.remove(layout[count - 1])
                layout.remove(layout[count - 2])
                layout.remove(layout[count - 3])
                layout.remove(layout[count - 4])

            elif (layoutCardMatches == 0 and 
                  self.stackPairMatchesStockPile(layout, stockPile)):

                count = len(layout)
                layout.insert(count - 2, choosenCard)

                stockPile.remove(choosenCard)
        
        self.setScore(score)