##############################################################
# Name:  Bryan Francis
# Project : GoStop Python
# Class : OPL Spring 2020
# Date : 3/27/2020
##############################################################

class Card(object):

##############################################################
# Function Name: Constructor
# Purpose: Constructor
# Parameters: 
#           self, int suit, int face, string card = None
# Assistance Received: None
##############################################################
    def __init__(self, suit, face, card = None):
        self.suitNames = ["S", "C", "D", "H", ""]
        self.faceNames = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K", "[", "]"]
        
        self.suit = suit
        self.face = face

        if card != None:
            for suit in range(4):
                for face in range(13):
                    if (self.faceNames[face] + self.suitNames[suit]) == card:
                        self.setFace(face)
                        self.setSuit(suit)

##############################################################
# Function Name: getFace
# Purpose: returns the face of the card
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def getFace(self):
        return self.face

##############################################################
# Function Name: getSuit
# Purpose: returns the suit of the card
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def getSuit(self):
        return self.suit

##############################################################
# Function Name: setFace
# Purpose: sets the face
# Parameters: 
#           self, int face
# Assistance Received: None
##############################################################
    def setFace(self, face):
        self.face = face

##############################################################
# Function Name: setSuit
# Purpose: sets the suit
# Parameters: 
#           self, int face
# Assistance Received: None
##############################################################
    def setSuit(self, suit):
        self.suit = suit

##############################################################
# Function Name: compareFace
# Purpose: compares face of two cards
# Parameters: 
#           self, faceToCompare
# Assistance Received: None
##############################################################
    def compareFace(self, faceToCompare):
        if((self.faceNames[self.face]) == faceToCompare):
            return 1
        else:
           return 0

##############################################################
# Function Name: print
# Purpose: prints the card
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def print(self):
        print ("{}{}" .format(self.faceNames[self.face], self.suitNames[self.suit]), end = " ")

##############################################################
# Function Name: cardMatcher
# Purpose: returns a string of the face and suit
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def cardMatcher(self):
        return self.faceNames[self.face] + self.suitNames[self.suit]


        