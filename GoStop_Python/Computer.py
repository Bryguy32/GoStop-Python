##############################################################
# Name:  Bryan Francis
# Project : GoStop Python
# Class : OPL Spring 2020
# Date : 3/27/2020
##############################################################
from Player import Player 
from Deck import Deck
from Card import Card

class Computer(Player):

##############################################################
# Function Name: Constructor
# Purpose: Constructor
# Parameters: 
#           self, score = 0
# Assistance Received: None
##############################################################
    def __init__(self, score = 0):
        self.deck = Deck()
        Player.__init__(self, score = 0)

##############################################################
# Function Name: Play
# Purpose: Makes a move for the computer
# Parameters: 
#           self, stockPile, layout, computerDeck, computerCapture, humanCapture
# Assistance Received: None
##############################################################
    def play(self, stockPile, layout, computerDeck, computerCapture, humanCapture):
        cardMatches = 0
        score = self.getScore()
        isCard = False
        hasCard = False
        cardPosition = 0
        playCard = ""

        if self.tripleCap(layout, computerDeck) == True:
            cardPosition = self.getCardPosition()
            print("The computer chose to play:", computerDeck[cardPosition].cardMatcher(),
                  "to capture all four cards")

        elif self.stackPair(layout, computerDeck, computerCapture):
            cardPosition = self.getCardPosition()
            print("The computer chose to play:", computerDeck[cardPosition].cardMatcher(),
                  "to create a stack pair")

        elif self.block(layout, computerDeck, humanCapture):
            cardPosition = self.getCardPosition()
            print("The computer chose to play:", computerDeck[cardPosition].cardMatcher(),
                  "to block you from capture the cards you need")

        elif self.pairFromStockPile(computerDeck, stockPile):
            cardPosition = self.getCardPosition()
            print("The computer chose to play:", computerDeck[cardPosition].cardMatcher(),
                  "to create a stack piar with the stock pile")
        else:
            print("The computer chose to play:", computerDeck[cardPosition].cardMatcher())

        playCard = computerDeck[cardPosition].cardMatcher()
        for computerD in computerDeck:

            if (computerD.cardMatcher() == playCard.upper()):

                choosenCard = computerD

                for j, lay in enumerate(layout):

                    if (computerD.getFace() == lay.getFace()):

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
            computerDeck.remove(choosenCard)

        elif (cardMatches == 1):

            card =  Card(4, 13)
            layout.append(card)
            layout.append(choosenCard)
            layout.append(layoutMatch1)
            card = Card(4, 14)
            layout.append(card)

            computerDeck.remove(choosenCard)
            layout.remove(layoutMatch1)

        elif (cardMatches == 2):

            print("Card to make a stack pair with:", end = " ")
            layoutMatch1.print()
            layoutMatch2.print()
            print()
            print("THe card entered is:", layoutMatch1.cardMatcher())

            card =  Card(4, 13)
            layout.append(card)
            layout.append(choosenCard)
            layout.append(layoutMatch1)
            card = Card(4, 14)
            layout.append(card)

            computerDeck.remove(choosenCard)
            layout.remove(layoutMatch1)

        elif (cardMatches == 3 or 
              self.tripleCapPositions(layout, choosenCard)):

            if (cardMatches == 3):

                computerCapture.append(choosenCard)
                computerCapture.append(layoutMatch1)
                computerCapture.append(layoutMatch2)
                computerCapture.append(layoutMatch3)

                computerDeck.remove(choosenCard)
                layout.remove(layoutMatch3)
                layout.remove(layoutMatch2)
                layout.remove(layoutMatch1)

            else:

                capPos = self.getTripCapPos()

                computerCapture.append(choosenCard)
                computerCapture.append(layout[capPos[0]])
                computerCapture.append(layout[capPos[1]])
                computerCapture.append(layout[capPos[2]])

                computerDeck.remove(choosenCard)

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

                computerCapture.append(choosenCard)
                computerCapture.append(layoutMatch1)

                count = 0
                for i in computerCapture:

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
                print("THe card entered is:", layoutMatch1.cardMatcher())
                
                # Add cards
                computerCapture.append(choosenCard)
                computerCapture.append(layoutMatch1)

                # Score
                count = 0
                for i in computerCapture:

                    if choosenCard.getFace() == computerCapture.getFace():

                        count += 1

                        if (count == 4 or count == 8):

                            score += 1

                # Erase cards
                stockPile.remove(choosenCard)
                layout.remove(layoutMatch1)

            elif (layoutCardMatches == 3 or 
                  self.tripleCapPositions(layout, choosenCard)):

                if (layoutCardMatches == 3):

                    computerCapture.append(choosenCard)
                    computerCapture.append(layoutMatch1)
                    computerCapture.append(layoutMatch2)
                    computerCapture.append(layoutMatch3)

                    # Erase cards
                    stockPile.remove(choosenCard)
                    layout.remove(layoutMatch1)                    
                    layout.remove(layoutMatch2)
                    layout.remove(layoutMatch3)

                else:

                    capPos = self.getTripCapPos()

                    computerCapture.append(choosenCard)
                    computerCapture.append(layout[capPos[0]])
                    computerCapture.append(layout[capPos[1]])
                    computerCapture.append(layout[capPos[2]])

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

                computerCapture.append(layout[count - 2])
                computerCapture.append(layout[count - 3])


                # Score
                scoreCount = 0
                for computerC in computerCapture:

                    if (layout[count - 2].getFace() == computerC.getFace()):

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

                    computerCapture.append(choosenCard)
                    computerCapture.append(layoutMatch1)                    
                    computerCapture.append(layoutMatch2)
                    computerCapture.append(layoutMatch3)

                    stockPile.remove(choosenCard)
                    layout.remove(layoutMatch3)
                    layout.remove(layoutMatch2)
                    layout.remove(layoutMatch1)

                else:

                    capPos = self.getTripCapPos()

                    computerCapture.append(choosenCard)
                    computerCapture.append(layout[capPos[0]])
                    computerCapture.append(layout[capPos[1]])
                    computerCapture.append(layout[capPos[2]])

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

                computerCapture.append(layout[count -2])
                computerCapture.append(layout[count - 3])

                # Score

                scoreCount = 0
                for computerC in computerCapture:

                    if (layout[count - 2].getFace() == computerC.getFace()):

                        scoreCount += 1

                        if (scoreCount == 4 or scoreCount == 8):

                            score += 1

                layout.remove(layout[count - 1])               
                layout.remove(layout[count - 2])
                layout.remove(layout[count - 3])
                layout.remove(layout[count - 4])

            elif (layoutCardMatches == 1 or layoutCardMatches == 2):

                # Add cards
                computerCapture.append(choosenCard)
                computerCapture.append(layoutMatch1)

                # Add stacked pair
                count = len(layout)
                computerCapture.append(layout[count - 2])
                computerCapture.append(layout[count - 3])

                # Check for four matching cards from stock pile card
                scoreCount = 0
                for humanCap in computerCapture:
                    if (choosenCard.getFace() == humanCap.getFace()):

                        scoreCount += 1

                        if (scoreCount == 4 or scoreCount == 8):

                            score += 1

                # Check for matching cards from stack pair
                # only if stack pair and stock pile cards are different
                if choosenCard.getFace() != layout[count - 2].getFace():
                    scoreCount = 0
                    for humanC in computerCapture:

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