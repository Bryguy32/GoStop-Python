##############################################################
# Name:  Bryan Francis
# Project : GoStop Python
# Class : OPL Spring 2020
# Date : 3/27/2020
##############################################################
from Card import Card
from Deck import Deck
from Player import Player
from Human import Human
from Computer import Computer
from Serialization import Serialization


class Round(object):
    
##############################################################
# Function Name: Constructor
# Purpose: Constructor
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def __init__(self):
        self.roundNumber = 1
        self.stockPile = []
        self.layout = []

        self.humanHand = [[], [], []]
        self.computerHand = [[], [], []]
        self.humanCapture = [[], [], []]
        self.computerCapture = [[], [], []]
        self.numComPlayers = 0
        self.numHumPlayers = 0
        
        #Initalize classes here
        self.s = Serialization()
        self.deck = Deck()
        self.player = Player()
        self.computer1 = Computer()
        self.computer2 = Computer()
        self.computer3 = Computer()
        self.human1 = Human()
        self.human2 = Human()
        self.human3 = Human()

##############################################################
# Function Name: setRound
# Purpose: sets the round
# Parameters: 
#           self, int round
# Assistance Received: None
##############################################################         
    def setRound(self, round):
        self.roundNumber = round

##############################################################
# Function Name: getRound
# Purpose: returns the round
# Parameters: 
#           self
# Assistance Received: None
##############################################################        
    def getRound(self):
        return self.round

##############################################################
# Function Name: showCard
# Purpose: shows the hand
# Parameters: 
#           self, hand
# Assistance Received: None
##############################################################
    def showCard(self, hand):

        for c in hand:
            c.print()

##############################################################
# Function Name: setComputer
# Purpose: Sets computer information from file
# Parameters: 
#           self, score, hand, capture, players
# Assistance Received: None
##############################################################
    def setComputer(self, score, hand, capture, players):
        self.computer1.setScore(score[0])
        self.computer2.setScore(score[1])
        self.computer3.setScore(score[2])
        self.computerHand = hand
        self.computerCapture = capture
        self.numComPlayers = players

##############################################################
# Function Name: setHuman
# Purpose: Sets human information from file
# Parameters: 
#           self, int face
# Assistance Received: None
##############################################################
    def setHuman(self, score, hand, capture, players):
        self.human1.setScore(score[0])
        self.human2.setScore(score[1])
        self.human3.setScore(score[2])
        self.humanHand = hand
        self.humanCapture = capture
        self.numHumPlayers = players

##############################################################
# Function Name: setLayout
# Purpose: sets the layout
# Parameters: 
#           self, layout
# Assistance Received: None
##############################################################
    def setLayout(self, layout):
        self.layout = layout

##############################################################
# Function Name: setStockPile
# Purpose: sets the stockPile
# Parameters: 
#           self, stockPile
# Assistance Received: None
##############################################################
    def setStockPile(self, stockPile):
        self.stockPile = stockPile

##############################################################
# Function Name: setNextPlayer
# Purpose: sets the nextPlayer
# Parameters: 
#           self, nextPlayer
# Assistance Received: None
##############################################################
    def setNextPlayer(self, nextPlayer):
        if nextPlayer == "Human" or nextPlayer == "Human 1\n":
            self.human1.setTurn(True)

        elif nextPlayer == "Human 2\n":
            self.human2.setTurn(True)

        elif nextPlayer == "Human 3\n":
            self.human3.setTurn(True)

        elif nextPlayer == "Computer" or nextPlayer == "Computer 1\n":
            self.computer1.setTurn(True)

        elif nextPlayer == "Computer 2\n":
            self.computer2.setTurn(True)

        elif nextPlayer == "Computer 3\n":
            self.computer3.setTurn(True)
           

##############################################################
# Function Name: draw
# Purpose: draws a card from deck
# Parameters: 
#           self, hand
# Assistance Received: None
##############################################################
    def draw(self, hand):
      hand.append(self.stockPile.pop())
      return self

##############################################################
# Function Name: setUpPlayers
# Purpose: Sets the players and decks
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def setUpPlayers(self):
        while (self.numComPlayers + self.numHumPlayers > 4 or
               self.numComPlayers + self.numHumPlayers == 0
               or self.numComPlayers + self.numHumPlayers < 2):
            self.numComPlayers = int(input("How many how many computer players? (1-3): "))
            self.numHumPlayers = int(input("How many human Players? (1-3): "))

            if (self.numComPlayers + self.numHumPlayers > 4):
                print("Sorry there can only be four total players :(")
                
        
        #Get number of decks
        numofDecks = 0
        while (numofDecks == 0 or numofDecks < 2 or
               numofDecks > 4):
            numofDecks = int(input("How many decks would you like to play with? (2-4): "))

            if (numofDecks < 2 or numofDecks > 4):
                print("Sorry please try again")

        #Set up Decks
        self.deck.shuffle()
        self.stockPile = self.deck.getDeck()

        if numofDecks == 2:
            self.deck.shuffle()
            tempDeck1 = self.deck.getDeck()
            self.stockPile = self.stockPile + tempDeck1

        elif numofDecks == 3:
            self.deck.shuffle()
            tempDeck1 = self.deck.getDeck()
            self.deck.shuffle()
            tempDeck2 = self.deck.getDeck()
            self.stockPile = self.stockPile + tempDeck1 + tempDeck2

        elif numofDecks == 4:
            self.deck.shuffle()
            tempDeck1 = self.deck.getDeck()
            self.deck.shuffle()
            tempDeck2 = self.deck.getDeck()
            self.deck.shuffle()
            tempDeck3 = self.deck.getDeck()
            self.stockPile = self.stockPile + tempDeck1 + tempDeck2 + tempDeck3

        print(self.humanHand)

##############################################################
# Function Name: setUpRound
# Purpose: sets up the round
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def setUpRound(self):
        #Distribute the cards to all the hands
        i = 0
        while i < self.numHumPlayers:
            for j in range(5):
                self.draw(self.humanHand[i])
            i += 1
        
        i = 0
        while i < self.numComPlayers:
            for j in range(5):
                self.draw(self.computerHand[i])
            i += 1

        for j in range(4):
            self.draw(self.layout)

        i = 0
        while i < self.numHumPlayers:
            for j in range(5):
                self.draw(self.humanHand[i])
            i += 1

        i = 0 
        while i < self.numComPlayers:
            for j in range(5):
                self.draw(self.computerHand[i])
            i += 1

        for j in range(4):
            self.draw(self.layout)

##############################################################
# Function Name: determinePlayer
# Purpose: determines player based off hand
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def determinePlayer(self):

        human1Count = 0
        human2Count = 0
        human3Count = 0
        computer1Count = 0
        computer2Count = 0
        computer3Count = 0

        j = 0
        highestCard = ["K", "Q", "J", "X", "9", "8", "7", "6", "5", "4", "3", "2", "A"]

        # If the round == 1 or the scores are equal
        # Loop through the deck of each player to
        # determine who has a better hand, the better
        # hand goes first

        if(self.roundNumber == 1):

            while True:
                num = 0
                while num < self.numHumPlayers:
                    for humH in self.humanHand[num]:
                        if humH.compareFace(highestCard[j]):
                            if num == 0:
                                human1Count += 1
                            elif num == 1:
                                human2Count += 1
                            elif num == 3:
                                human3Count += 1
                    num += 1

                num = 0
                while num < self.numComPlayers:
                    for comH in self.computerHand[num]:
                        if comH.compareFace(highestCard[j]):
                            if num == 0:
                                computer1Count += 1
                            elif num == 1:
                                computer2Count += 1
                            elif num == 3:
                                computer3Count += 1
                    num += 1
                
                if (human1Count > computer1Count and
                    human1Count > computer2Count and
                    human1Count > computer3Count and
                    human1Count > human2Count and
                    human1Count > human3Count):

                    print("Human 1has the better hand and will start\n")
                    self.human1.setTurn(True)
                    break
                
                elif (human2Count > computer1Count and
                      human2Count > computer2Count and
                      human2Count > computer3Count and
                      human2Count > human3Count):

                    print("Human 2 has the better hand and will start\n")
                    self.human2.setTurn(True)
                    break

                elif (human3Count > computer1Count and
                      human3Count > computer2Count and
                      human3Count > computer3Count):

                    print("Human 3 has the better hand and will start\n")
                    self.human3.setTurn(True)
                    break

                elif (computer1Count > computer2Count and
                      computer1Count > computer3Count):

                    print("Computer 1 has the better hand and will start\n")
                    self.computer1.setTurn(True)
                    break

                elif (computer2Count > computer3Count):

                    print("Computer 2 has the better hand and will start\n")
                    self.computer2.setTurn(True)
                    break

                elif (computer3Count > computer2Count):

                    print("Computer 3 has the better hand and will start\n")
                    self.computer3.setTurn(True)
                    break

                if (j == 13):
                    print("All card mathced the round is starting over\n")
                    round = Round()

                j += 1
                
        
        elif (self.roundNumber > 1):

            if(self.human1.getScore() > self.computer1.getScore() and
               self.human1.getScore() > self.computer2.getScore() and 
               self.human1.getScore() > self.computer3.getScore() and 
               self.human1.getScore() > self.human2.getScore() and 
               self.human1.getScore() > self.human3.getScore()):

                self.human1.setTurn(True)
                self.human2.setTurn(False)                
                self.human3.setTurn(False)
                self.computer1.setTurn(False)              
                self.computer2.setTurn(False)
                self.computer3.setTurn(False)

            elif (self.human2.getScore() > self.computer1.getScore() and 
                  self.human2.getScore() > self.computer2.getScore() and 
                  self.human2.getScore() > self.computer3.getScore() and 
                  self.human2.getScore() > self.human3.getScore()):

                self.human1.setTurn(False)
                self.human2.setTurn(True)                
                self.human3.setTurn(False)
                self.computer1.setTurn(False)              
                self.computer2.setTurn(False)
                self.computer3.setTurn(False)

            elif (self.human3.getScore() > self.computer1.getScore() and 
                  self.human3.getScore() > self.computer2.getScore() and 
                  self.human3.getScore() > self.computer3.getScore()):

                self.human1.setTurn(False)
                self.human2.setTurn(False)                
                self.human3.setTurn(True)
                self.computer1.setTurn(False)              
                self.computer2.setTurn(False)
                self.computer3.setTurn(False)

            elif (self.computer1.getScore() > self.computer2.getScore() and
                  self.computer1.getScore() > self.computer3.getScore()):

                self.human1.setTurn(False)
                self.human2.setTurn(False)                
                self.human3.setTurn(False)
                self.computer1.setTurn(True)              
                self.computer2.setTurn(False)
                self.computer3.setTurn(False)

            elif (self.computer2.getScore() > self.computer2.getScore()):

                self.human1.setTurn(False)
                self.human2.setTurn(False)                
                self.human3.setTurn(False)
                self.computer1.setTurn(False)              
                self.computer2.setTurn(True)
                self.computer3.setTurn(False)

            elif (self.computer3.getScore() > self.computer2.getScore()):

                self.human1.setTurn(False)
                self.human2.setTurn(False)                
                self.human3.setTurn(False)
                self.computer1.setTurn(False)              
                self.computer2.setTurn(False)
                self.computer3.setTurn(True)


##############################################################
# Function Name: nextPlayer
# Purpose: returns the next player
# Parameters: 
#           self, hand
# Assistance Received: None
##############################################################
    def nextPlayer(self):

         if self.human1.getIsTurn() == True:
            return "Human 1"

         elif self.human2.getIsTurn() == True:
            return "Human 2"

         elif self.human3.getIsTurn() == True:
            return "Human 3"

         elif self.computer1.getIsTurn() == True:
            return "Computer 1"

         elif self.computer2.getIsTurn() == True:
            return "Computer 2"

         elif self.computer3.getIsTurn() == True:
            return "Computer 3"
##############################################################
# Function Name: display
# Purpose: shows the display
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def display(self):
        
        print()
        print("---------------------------")

        print("Round:", self.roundNumber)
        print()

        #Computer
        print("Computer 1:")
        print("Score:", self.computer1.getScore())
        print("Hand:", end=" ")
        self.showCard(self.computerHand[0])
        print()
        print("Capture Pile:", end=" ")
        self.showCard(self.computerCapture[0])

        #Human
        print("\n")
        print("Human 1:")
        print("Score:", self.human1.getScore())
        print("Hand:", end=" ")
        self.showCard(self.humanHand[0])
        print()
        print("Capture Pile:", end=" ")
        self.showCard(self.humanCapture[0])
        print("\n")

        #Computer2
        if self.numComPlayers >= 2:
            print("Computer 2:")
            print("Score:", self.computer2.getScore())
            print("Hand:", end=" ")
            self.showCard(self.computerHand[1])
            print()
            print("Capture Pile:", end=" ")
            self.showCard(self.computerCapture[1])

        #Human 2
        if self.numHumPlayers >=2:
            print("\n")
            print("Human 2:")
            print("Score:", self.human2.getScore())
            print("Hand:", end=" ")
            self.showCard(self.humanHand[1])
            print()
            print("Capture Pile:", end=" ")
            self.showCard(self.humanCapture[1])
            print("\n")

        #Computer 3
        if self.numComPlayers == 3:
            print("Computer 2:")
            print("Score:", self.computer3.getScore())
            print("Hand:", end=" ")
            self.showCard(self.computerHand[2])
            print()
            print("Capture Pile:", end=" ")
            self.showCard(self.computerCapture[2])

        #Human 3
        if self.numHumPlayers == 3:
            print("\n")
            print("Human 3:")
            print("Score:", self.human3.getScore())
            print("Hand:", end=" ")
            self.showCard(self.humanHand[2])
            print()
            print("Capture Pile:", end=" ")
            self.showCard(self.humanCapture[2])
            print("\n")


        #Layout
        print("Layout:", end=" ")
        self.showCard(self.layout)
        print("\n")
        
        #Stock pile
        print("Stock Pile:", end=" ")
        self.showCard(self.stockPile)

        #Next Player
        print("\n")
        print("Next Player:", end=" ")
        print(self.nextPlayer())
        print("--------\n")
        self.menu()

##############################################################
# Function Name: menu
# Purpose: menu for human
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def menu(self):

        if sum(len(x) for x in self.humanHand) == 0 and sum(len(y) for y in self.computerHand) == 0:
            self.nextRound()

        #Check to make sure hand is not empty of current player
        self.checkHand()

        if (self.computer1.getIsTurn() == True):
            self.computerMenu()
            return
        
        elif (self.computer2.getIsTurn() == True):
            self.computerMenu()
            return

        elif (self.computer3.getIsTurn() == True):
            self.computerMenu()
            return


        print("1. Save the game")
        print("2. Make a move")
        print("3. Ask for help")
        print("4. Quit the game")

        while True:

            selection = int(input("Selection: "))
            if(selection > 0 and selection < 5):
                break

        if selection == 1:
            computerScores = [0,0,0]
            humanScores = [0,0,0]
            nextPlayer = self.nextPlayer()

            print("Save the game")
            #Computer Scores
            computerScores[0] = self.computer1.getScore()
            if self.numComPlayers >= 2:
                computerScores[1] = self.computer2.getScore()
            if self.numComPlayers == 3:
                computerScores[2] = self.computer3.getScore()

            #Human Scores
            humanScores[0] = self.human1.getScore()
            if self.numHumPlayers >= 2:
                humanScores[1] = self.human2.getScore()
            if self.numHumPlayers == 3:
                humanScores[2] = self.human3.getScore()

            self.s.saveGame(self.roundNumber, computerScores, self.computerHand, self.computerCapture, self.numComPlayers,
                            humanScores, self.humanHand, self.humanCapture, self.numHumPlayers,
                           self.layout, self.stockPile, nextPlayer)
            #Save the Game

        elif selection == 2:

            self.move()

        elif selection == 3:

            if (self.human1.getIsTurn() == True):
                self.player.play(self.stockPile, self.layout, self.humanHand[0],
                            self.humanCapture[0], self.computerCapture[0])

            elif (self.human2.getIsTurn() == True):
                self.player.play(self.stockPile, self.layout, self.humanHand[1],
                            self.humanCapture[1], self.computerCapture[0])

            elif (self.human3.getIsTurn() == True):
                self.player.play(self.stockPile, self.layout, self.humanHand[2],
                            self.humanCapture[2], self.computerCapture[0])
            self.menu()

        elif selection == 4:

            self.endGame()

##############################################################
# Function Name: computerMenu
# Purpose: Menu for computer
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def computerMenu(self):

        print("1. Save Game")
        print("2. Computer Move")
        print("3. Quit Game")

        while True:

            selection = int(input("Selection: "))
            if (selection > 0 and selection < 4):
                break

        if selection == 1:
            computerScores = [0,0,0]
            humanScores = [0,0,0]
            nextPlayer = self.nextPlayer()

            print("Save the game")
            #Computer Scores
            computerScores[0] = self.computer1.getScore()
            if self.numComPlayers >= 2:
                computerScores[1] = self.computer2.getScore()
            if self.numComPlayers == 3:
                computerScores[2] = self.computer3.getScore()

            #Human Scores
            humanScores[0] = self.human1.getScore()
            if self.numHumPlayers >= 2:
                humanScores[1] = self.human2.getScore()
            if self.numHumPlayers == 3:
                humanScores[2] = self.human3.getScore()

            self.s.saveGame(self.roundNumber, computerScores, self.computerHand, self.computerCapture, self.numComPlayers,
                            humanScores, self.humanHand, self.humanCapture, self.numHumPlayers,
                           self.layout, self.stockPile, nextPlayer)
            print("Save the game")

        elif selection == 2:

            self.move()

        elif selection == 3:

            self.endGame()

##############################################################
# Function Name: switchPlayer
# Purpose: switches current player
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def switchPlayer(self):
        #Order alternates com hum, com, hum
        if (self.computer1.getIsTurn() == True):
            self.computer1.setTurn(False)
            self.human1.setTurn(True)
          
        elif (self.human1.getIsTurn() == True):
            self.human1.setTurn(False)
            if self.numComPlayers >= 2:
                self.computer2.setTurn(True)
            elif self.numHumPlayers >= 2:
                self.human2.setTurn(True)
            else:
                self.computer1.setTurn(True)

        elif (self.computer2.getIsTurn() == True):
            self.computer2.setTurn(False)
            if self.numHumPlayers >= 2:
                self.human2.setTurn(True)
            elif self.numComPlayers == 3:
                self.computer3.setTurn(True)
            else:
                self.human1.setTurn(True)

        elif (self.human2.getIsTurn() == True):
            self.human2.setTurn(False)
            if self.numComPlayers == 3:
                self.computer3.setTurn(True)
            elif self.numHumPlayers == 3:
                self.human3.setTurn(True)
            else:
                self.computer1.setTurn(True)

        elif (self.computer3.getIsTurn() == True):
            self.computer3.setTurn(False)
            if self.numHumPlayers == 3:
                self.human3.setTurn(True)
            else:
                self.human1.setTurn(True)

        elif (self.human3.getIsTurn() == True):
            self.human3.setTurn(False)
            self.computer1.setTurn(True)


##############################################################
# Function Name: checkHand
# Purpose: switches current player if no cards in hand
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def checkHand(self):

        if(self.computer1.getIsTurn() and len(self.computerHand[0]) == 0):
            print("Hand is empty, moving to next player")
            self.switchPlayer()
        

        elif(self.computer2.getIsTurn() and len(self.computerHand[1]) == 0):
            print("Hand is empty, moving to next player")
            self.switchPlayer()

        elif(self.computer3.getIsTurn() and len(self.computerHand[2]) == 0):
            print("Hand is empty, moving to next player")
            self.switchPlayer()

        elif(self.human1.getIsTurn() and len(self.humanHand[0]) == 0):
            print("Hand is empty, moving to next player")
            self.switchPlayer()

        elif(self.human2.getIsTurn() and len(self.humanHand[1]) == 0):
            print("Hand is empty, moving to next player")
            self.switchPlayer()

        elif(self.human3.getIsTurn() and len(self.humanHand[2]) == 0):
            print("Hand is empty, moving to next player")
            self.switchPlayer()





 
##############################################################
# Function Name: move
# Purpose: Makes a move for current player
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def move(self):
        
        if (self.computer1.getIsTurn() == True):
            self.computer1.play(self.stockPile, self.layout, self.computerHand[0], self.computerCapture[0], self.humanCapture[0])

        elif (self.computer2.getIsTurn() == True):
            self.computer2.play(self.stockPile, self.layout, self.computerHand[1], self.computerCapture[1], self.humanCapture[0])

        elif (self.computer3.getIsTurn() == True):
            self.computer3.play(self.stockPile, self.layout, self.computerHand[2], self.computerCapture[2], self.humanCapture[0])

        elif (self.human1.getIsTurn() == True):
            self.human1.play(self.stockPile, self.layout, self.humanHand[0], self.humanCapture[0])

        elif (self.human2.getIsTurn() == True):
            self.human2.play(self.stockPile, self.layout, self.humanHand[1], self.humanCapture[1])

        elif (self.human3.getIsTurn() == True):
            self.human3.play(self.stockPile, self.layout, self.humanHand[2], self.humanCapture[2])

        self.switchPlayer()
        self.display()

##############################################################
# Function Name: nextRound
# Purpose: starts the next round
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def nextRound(self):
        str = ""
        while(str != "YES" and str != "NO"):
            str = input("The round is over would you like to play another round? (Yes or No): ")
            str = str.upper()

        if str == "YES":
            self.computerHand = [[],[],[]]
            self.humanHand = [[],[],[]]
            self.layout.clear()
            self.stockPile.clear()
            self.humanCapture = [[],[],[]]
            self.computerCapture = [[],[],[]]

            self.roundNumber += 1
            self.setUpPlayers()
            self.setUpRound()
            self.determinePlayer()
            self.display()

        else:
            self.endGame()

##############################################################
# Function Name: endGame
# Purpose: ends the game
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def endGame(self):

        if(self.human1.getScore() == self.computer1.getScore() and
               self.human1.getScore() == self.computer2.getScore() and 
               self.human1.getScore() == self.computer3.getScore() and 
               self.human1.getScore() == self.human2.getScore() and 
               self.human1.getScore() == self.human3.getScore()):

           print("TIE GAME")

        elif(self.human1.getScore() > self.computer1.getScore() and
               self.human1.getScore() > self.computer2.getScore() and 
               self.human1.getScore() > self.computer3.getScore() and 
               self.human1.getScore() > self.human2.getScore() and 
               self.human1.getScore() > self.human3.getScore()):

            print("Congrats Human 1 you won!")

        elif (self.human2.getScore() > self.computer1.getScore() and 
                  self.human2.getScore() > self.computer2.getScore() and 
                  self.human2.getScore() > self.computer3.getScore() and 
                  self.human2.getScore() > self.human3.getScore()):

            print("Congrats Human 2 you won!")

        elif (self.human3.getScore() > self.computer1.getScore() and 
                  self.human3.getScore() > self.computer2.getScore() and 
                  self.human3.getScore() > self.computer3.getScore()):

            print("Congrats Human 3 you won!")

        elif (self.computer1.getScore() > self.computer2.getScore() and
                  self.computer1.getScore() > self.computer3.getScore()):

            print("Computer 1 has won")

        elif (self.computer2.getScore() > self.computer2.getScore()):

            print("Computer 2 has won")

        elif (self.computer3.getScore() > self.computer2.getScore()):

            print("Computer 3 has won")

