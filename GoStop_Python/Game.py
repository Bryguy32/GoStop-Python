##############################################################
# Name:  Bryan Francis
# Project : GoStop Python
# Class : OPL Spring 2020
# Date : 3/27/2020
##############################################################
from Round import Round
from Serialization import Serialization

class Game(object):

##############################################################
# Function Name: Constructor
# Purpose: Constructor
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def __init__(self):
        self.round = Round()
        self.s = Serialization()

##############################################################
# Function Name: startGame
# Purpose: starts the game
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def startGame(self):
        choice = 0
        while choice < 1 or choice > 2 or choice == 0:
            print("(1) Start new Game")
            print("(2) Load Game")
            choice = int(input("Selection: "))

            if choice < 1 or choice > 2:
                print("Please enter a valid input")

        if choice == 1:
            self.round.setUpPlayers()
            self.round.setUpRound()
            self.round.determinePlayer()
            self.round.display()

        elif choice == 2:
            self.resumeGame()
            self.round.display()

##############################################################
# Function Name: resumeGame
# Purpose: loads game from file
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def resumeGame(self):
        comScore = [0,0,0]
        humScore = [0,0,0]
        humHand = [[],[],[]]
        humCapture = [[],[],[]]
        computerHand = [[],[],[]]
        computerCapture = [[],[],[]]
        layout = []
        stockPile = []
        numComPlayers = 0
        numHumanPlayers = 0
        nextPlayer = ""
        fileName = input("What is the name of the file you would like to resume: ")
        self.s.setFileName(fileName)

        #Round
        roundNum = self.s.getRound()
        self.round.setRound(roundNum)  

        #Computer and Human        
        comScore, computerHand, computerCapture, numComPlayers = self.s.getComputer()
        self.round.setComputer(comScore, computerHand, computerCapture, numComPlayers)
        humScore, humHand, humCapture, numHumanPlayers = self.s.getHuman()
        self.round.setHuman(humScore, humHand, humCapture, numHumanPlayers)
    
        #Layout and Stock Pile
        layout = self.s.getLayout()
        self.round.setLayout(layout)
        stockPile = self.s.getStockPile()
        self.round.setStockPile(stockPile)

        #Next Player
        nextPlayer = self.s.getNextPlayer()
        self.round.setNextPlayer(nextPlayer)



