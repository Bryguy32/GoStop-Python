##############################################################
# Name:  Bryan Francis
# Project : GoStop Python
# Class : OPL Spring 2020
# Date : 3/27/2020
##############################################################
from Card import Card
import random

class Deck(object):

##############################################################
# Function Name: Constructor
# Purpose: Constructor
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def __init__(self):
        self.cards = []
        
        for suit in range(4):
            for face in range(13):

                card =  Card(suit, face)
                self.cards.append(card)

##############################################################
# Function Name: getDeck
# Purpose: sets the face
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def getDeck(self):
        return self.cards

##############################################################
# Function Name: setDeck
# Purpose: sets the deck
# Parameters: 
#           self, cards
# Assistance Received: None
##############################################################
    def setDeck(self, cards):
        self.cards = cards

##############################################################
# Function Name: shuffle
# Purpose: shuffles the deck
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

##############################################################
# Function Name: printList
# Purpose: prints the list
# Parameters: 
#           self, list hand
# Assistance Received: None
##############################################################
    def printList(self, hand):
    
            for c in hand:
                c.print()

