##############################################################
# Name:  Bryan Francis
# Project : GoStop Python
# Class : OPL Spring 2020
# Date : 3/27/2020
##############################################################
from Card import Card
class Serialization(object):

##############################################################
# Function Name: Constructor
# Purpose: Constructor
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def __init__(self):
        self.fileName = ""

##############################################################
# Function Name: setFileName
# Purpose: sets the file name
# Parameters: 
#           self, fileName
# Assistance Received: None
##############################################################
    def setFileName(self, fileName):
        self.fileName = fileName

##############################################################
# Function Name: saveGame
# Purpose: saves the game to file
# Parameters: 
#           self, round, computerScore, computerDeck, computerCapture,
# computerPlayers, humanScore, humanDeck, humanCapture, humanPlayers,
# layout, stockPile, nextPlayer
# Assistance Received: None
##############################################################
    def saveGame(self, round, computerScore, computerDeck, computerCapture, computerPlayers, humanScore, 
                 humanDeck, humanCapture, humanPlayers, layout, stockPile, nextPlayer):

        fileName = input("Please enter a filename: ")
        fileW = open(fileName, "w")

        roundW = ["Round: ", str(round), "\n"]
        fileW.writelines(roundW)
        fileW.write("\n")
        fileW.write("\n")

        #Computer 1
        fileW.write("Computer 1:\n")
        computerS = ["   Score: ", str(computerScore[0]), "\n"]
        fileW.writelines(computerS)
        fileW.write("   Hand: ")
        for element in computerDeck[0]:
            fileW.write(element.cardMatcher())
            fileW.write(" ")
        fileW.write("\n")
        fileW.write("   Capture Pile: ")
        for element in computerCapture[0]:
            fileW.write(element.cardMatcher())
            fileW.write(" ")
        fileW.write("\n")
        fileW.write("\n")

        #Human 1
        fileW.write("Human 1:\n")
        humanS = ["   Score: ", str(humanScore[0]), "\n"]
        fileW.writelines(humanS)
        fileW.write("   Hand: ")
        for element in humanDeck[0]:
            fileW.write(element.cardMatcher())
            fileW.write(" ")
        fileW.write("\n")
        fileW.write("   Capture Pile: ")
        for element in humanCapture[0]:
            fileW.write(element.cardMatcher())
            fileW.write(" ")
        fileW.write("\n")
        fileW.write("\n")

        #Computer 2
        if computerPlayers >= 2:
            fileW.write("Computer 2:\n")
            computerS = ["   Score: ", str(computerScore[1]), "\n"]
            fileW.writelines(computerS)
            fileW.write("   Hand: ")
            for element in computerDeck[1]:
                fileW.write(element.cardMatcher())
                fileW.write(" ")
            fileW.write("\n")
            fileW.write("   Capture Pile: ")
            for element in computerCapture[1]:
                fileW.write(element.cardMatcher())
                fileW.write(" ")
            fileW.write("\n")
            fileW.write("\n")

        # Human 2
        if humanPlayers >= 2:
            fileW.write("Human 2:\n")
            humanS = ["   Score: ", str(humanScore[1]), "\n"]
            fileW.writelines(humanS)
            fileW.write("   Hand: ")
            for element in humanDeck[1]:
                fileW.write(element.cardMatcher())
                fileW.write(" ")
            fileW.write("\n")
            fileW.write("   Capture Pile: ")
            for element in humanCapture[1]:
                fileW.write(element.cardMatcher())
                fileW.write(" ")
            fileW.write("\n")
            fileW.write("\n")

         #Computer 3
        if computerPlayers == 3:
            fileW.write("Computer 3:\n")
            computerS = ["   Score: ", str(computerScore[2]), "\n"]
            fileW.writelines(computerS)
            fileW.write("   Hand: ")
            for element in computerDeck[2]:
                fileW.write(element.cardMatcher())
                fileW.write(" ")
            fileW.write("\n")
            fileW.write("   Capture Pile: ")
            for element in computerCapture[2]:
                fileW.write(element.cardMatcher())
                fileW.write(" ")
            fileW.write("\n")
            fileW.write("\n")

        # Human 3
        if humanPlayers == 3:
            fileW.write("Human 3:\n")
            humanS = ["   Score: ", str(humanScore[1]), "\n"]
            fileW.writelines(humanS)
            fileW.write("   Hand: ")
            for element in humanDeck[2]:
                fileW.write(element.cardMatcher())
                fileW.write(" ")
            fileW.write("\n")
            fileW.write("   Capture Pile: ")
            for element in humanCapture[2]:
                fileW.write(element.cardMatcher())
                fileW.write(" ")
            fileW.write("\n")
            fileW.write("\n")

        #Layout
        fileW.write("Layout: ")
        for element in layout:
            fileW.write(element.cardMatcher())
            fileW.write(" ")
        fileW.write("\n")
        fileW.write("\n")

        #Stock Pile
        fileW.write("Stock Pile: ")
        for element in stockPile:
            fileW.write(element.cardMatcher())
            fileW.write(" ")
        fileW.write("\n")
        fileW.write("\n")

        #Next Player
        fileW.write("Next Player: ")
        fileW.write(nextPlayer)

        fileW.close()

##############################################################
# Function Name: getRound
# Purpose: get round from file
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def getRound(self):

        reader = open(self.fileName, "r")
        try:

            for line in reader:
                for word in line.split():
                    if word == "Round:":
                        continue
                roundNum = int(word)
                break

        finally:
            reader.close()
            return roundNum

##############################################################
# Function Name: getNextPlayer
# Purpose: get next player from file
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def getNextPlayer(self):

        reader = open(self.fileName, "r")
        isNextPlayer = False
        try:
            for line in reader:
                for word in line.split():
                    if word == "Next":
                        isNextPlayer = True

                    if word == "Player:" and isNextPlayer == True:
                        line = line.replace("Next Player: ", "")
                        nextPlayer = line
                        isNextPlayer = False

        finally:
            reader.close()
            return nextPlayer

##############################################################
# Function Name: getComputer
# Purpose: get computer from file
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def getComputer(self):
        numComPlayer = 0
        score = [0,0,0]
        computerHand = [[], [], []]
        computerCapture = [[], [], []]
        isComputer = False
        isScore = False
        isHand = False
        isCapture = False

        reader = open(self.fileName, "r")
        try:
            for line in reader:
                for word in line.split():
                    if line == "Computer 1:\n" or line == "Computer:\n":
                        numComPlayer += 1
                        #Loop 3 times for score, hand and capture
                        i = 0
                        while i < 3:
                           line = reader.readline()
                           for word in line.split():
                               if word == "Score:":
                                   isScore = True
                                   continue
                               if isScore:
                                   score[0] = int(word)
                                   isScore = False

                               if word == "Hand:":
                                   isHand = True
                                   continue
                               if isHand:
                                   line = line.replace("Hand:","")
                                   for word in line.split():
                                       card = Card(0,0,word)
                                       computerHand[0].append(card)
                                       isHand = False

                               if word == "Pile:":
                                   isCapture = True
                                   continue
                               if isCapture:
                                   line = line.replace("Capture Pile:","")
                                   for word in line.split():
                                       card = Card(0,0, word)
                                       computerCapture[0].append(card)
                                   isCapture = False
                           i += 1
                    elif line == "Computer 2:\n":
                       numComPlayer += 1
                       #Loop 3 times for score, hand and capture
                       i = 0
                       while i < 3:
                           line = reader.readline()
                           for word in line.split():
                               if word == "Score:":
                                   isScore = True
                                   continue
                               if isScore:
                                   score[1] = int(word)
                                   isScore = False

                               if word == "Hand:":
                                   isHand = True
                                   continue
                               if isHand:
                                   line = line.replace("Hand:","")
                                   for word in line.split():
                                       card = Card(0,0,word)
                                       computerHand[1].append(card)
                                       isHand = False

                               if word == "Pile:":
                                   isCapture = True
                                   continue
                               if isCapture:
                                   line = line.replace("Capture Pile:","")
                                   for word in line.split():
                                       card = Card(0,0,word)
                                       computerCapture[1].append(card)
                                   isCapture = False
                           i += 1
                    elif line == "Computer 3:\n":
                       numComPlayer += 1
                       #Loop 3 times for score, hand and capture
                       i = 0
                       while i < 3:
                           line = reader.readline()
                           for word in line.split():
                               if word == "Score:":
                                   isScore = True
                                   continue
                               if isScore:
                                   score[2] = int(word)
                                   isScore = False

                               if word == "Hand:":
                                   isHand = True
                                   continue
                               if isHand:
                                   line = line.replace("Hand:","")
                                   for word in line.split():
                                       card = Card(0,0, word)
                                       computerHand[2].append(card)
                                       isHand = False

                               if word == "Pile:":
                                   isCapture = True
                                   continue
                               if isCapture:
                                   line = line.replace("Capture Pile:","")
                                   for word in line.split():
                                       card = Card(0,0, word)
                                       computerCapture[2].append(card)
                                   isCapture = False
                           i += 1

        finally:
            reader.close()
            return score, computerHand, computerCapture, numComPlayer
  
##############################################################
# Function Name: getHuman
# Purpose: get human from file
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def getHuman(self):
        numHumPlayers = 0
        score = [0,0,0]
        humanHand = [[], [], []]
        humanCapture = [[], [], []]
        isHuman = False
        isScore = False
        isHand = False
        isCapture = False

        reader = open(self.fileName, "r")
        try:
            for line in reader:
                for word in line.split():
                    if line == "Human 1:\n" or line == "Human:\n":
                        numHumPlayers += 1
                        #Loop 3 times for score, hand and capture
                        i = 0
                        while i < 3:
                           line = reader.readline()
                           for word in line.split():
                               if word == "Score:":
                                   isScore = True
                                   continue
                               if isScore:
                                   score[0] = int(word)
                                   isScore = False

                               if word == "Hand:":
                                   isHand = True
                                   continue
                               if isHand:
                                   line = line.replace("Hand:","")
                                   for word in line.split():
                                       card = Card(0,0,word)
                                       humanHand[0].append(card)
                                       isHand = False

                               if word == "Pile:":
                                   isCapture = True
                                   continue
                               if isCapture:
                                   line = line.replace("Capture Pile:","")
                                   for word in line.split():
                                       card = Card(0,0, word)
                                       humanCapture[0].append(card)
                                   isCapture = False
                           i += 1
                    elif line == "Human 2:\n":
                       numHumPlayers += 1
                       #Loop 3 times for score, hand and capture
                       i = 0
                       while i < 3:
                           line = reader.readline()
                           for word in line.split():
                               if word == "Score:":
                                   isScore = True
                                   continue
                               if isScore:
                                   score[1] = int(word)
                                   isScore = False

                               if word == "Hand:":
                                   isHand = True
                                   continue
                               if isHand:
                                   line = line.replace("Hand:","")
                                   for word in line.split():
                                       card = Card(0,0,word)
                                       humanHand[1].append(card)
                                       isHand = False

                               if word == "Pile:":
                                   isCapture = True
                                   continue
                               if isCapture:
                                   line = line.replace("Capture Pile:","")
                                   for word in line.split():
                                       card = Card(0,0,word)
                                       humanCapture[1].append(card)
                                   isCapture = False
                           i += 1
                    elif line == "Human 3:\n":
                       numHumPlayers += 1
                       #Loop 3 times for score, hand and capture
                       i = 0
                       while i < 3:
                           line = reader.readline()
                           for word in line.split():
                               if word == "Score:":
                                   isScore = True
                                   continue
                               if isScore:
                                   score[2] = int(word)
                                   isScore = False

                               if word == "Hand:":
                                   isHand = True
                                   continue
                               if isHand:
                                   line = line.replace("Hand:","")
                                   for word in line.split():
                                       card = Card(0,0, word)
                                       humanHand[2].append(card)
                                       isHand = False

                               if word == "Pile:":
                                   isCapture = True
                                   continue
                               if isCapture:
                                   line = line.replace("Capture Pile:","")
                                   for word in line.split():
                                       card = Card(0,0, word)
                                       humanCapture[2].append(card)
                                   isCapture = False
                           i += 1

        finally:
            reader.close()
            return score, humanHand, humanCapture, numHumPlayers

##############################################################
# Function Name: getlayout
# Purpose: get layout from file
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def getLayout(self):
        layout = []
        reader = open(self.fileName, "r")
        try:
            for line in reader:
                for word in line.split():
                    if word == "Layout:":
                        line = line.replace("Layout:", "")
                        for word in line.split():
                            card = Card(0,0,word)
                            layout.append(card)

        finally:
            reader.close()
            return layout

##############################################################
# Function Name: getStockPile
# Purpose: get stock pile from file
# Parameters: 
#           self
# Assistance Received: None
##############################################################
    def getStockPile(self):
        stockPile = []
        isStockPile = False
        reader = open(self.fileName, "r")
        try:
            for line in reader:
                for word in line.split():
                    if word == "Stock":
                        isStockPile = True
                    if word == "Pile:" and isStockPile == True:
                        line = line.replace("Stock Pile:", "")
                        for word in line.split():
                            card = Card(0,0,word)
                            stockPile.append(card)
                        isStockPile = False

        finally:
            reader.close()
            return stockPile
                    
