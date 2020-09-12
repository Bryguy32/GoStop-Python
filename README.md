# GoStop-CPP
Go Stop is a card game played by 2 players. The Objective The objective of this game is to score the most points after all the rounds. The Players Two players play this game - one player will be the human user of your program, and the other player will be your program/computer. The Setup Two standard 52-card decks are used. Each player has a hand and a capture pile. In addition, a layout and stock pile are part of the game. A Round A round proceeds as follows: The two decks are shuffled together. The cards are dealt as follows: 5 cards are dealt to the human player; 5 cards are dealt to the computer player; 4 cards are placed face up in the layout; 5 cards are dealt to the human player; 5 cards are dealt to the computer player; 4 cards are placed face up in the layout; The remaining cards are left in the stock pile, face down. The first player is determined as follows: On the first round, the player with the most Kings plays first. If there is a tie, the player with the most Queens plays first. And so on down to the most Aces. If there is a tie in the number of Aces also, it means the two players have exactly the same set of cards (modulo suit). All the cards are collected back, the decks are reshuffled and the round is started all over again. On subsequent rounds, the player with the most points from previous rounds plays first. If there is a tie in points, the first player is determined using the mechanism described above for the first round. The two players take alternate turns thereafter till the round ends. The round ends when both players have played all the cards in their hands. A Turn During their turn, a player plays as follows: Plays a card from their hand. If the card matches: H0: no card in the layout, the card is added to the layout. H1: one card in the layout, the player creates a stack pair of the two cards and leaves it in the layout. H2: two cards in the layout, the player picks one of the two cards and creates a stack pair with it and the card played from the hand, leaving the stack pair in the layout. H3: three cards in the layout or triple stack, the player captures all four cards, i.e., adds them to their capture pile. Plays the top card from the stock pile. If this follows: H0 or H3 - If the card from the stock pile matches: no card in the layout, the card is added to the layout. one card in the layout, the player captures both the cards: the card played from the stock pile and the card from the layout that matches it. two cards in the layout, the player picks one of the two matching cards and captures it along with the card played from the stock pile. three cards in the layout or triple stack, the player captures all four cards. H1 or H2: If the card from the stock pile matches: no card in the layout, the card is added to the layout. The pair of cards stacked in H1/H2 are captured. three cards in the layout or triple stack, the player captures all four cards. The pair of cards stacked in H1/H2 are also captured. any card in the layout other than the stack pair from H1/H2, the player captures both the pairs - the stacked pair and the current pair. only the stack pair from H1/H2, the player does not capture any card - the player leaves all three cards as a triple stack in the layout. Two cards match if they have the same face (A-K). A Game A game consists of as many rounds as the human player wants to play. The human player is asked before each round whether the player wants to play another round. If the human player replies yes, another round is started. If the human player replies no, the game is ended and the player with the most points is declared the winner of the game. Score The player earns one point for each arrangement of all four matching cards in the player's capture pile when the round ends. Note that this could happen in one of two ways: The player captured a triple stack with a hand or stock card. The player captured two pairs (on two different occasions) that match with each other. So, the player has incentive to capture a pair that matches an earlier captured pair. Computer Player's Strategy Your computer player must play to win. It must have a strategy for which card to play from its hand. Implementation Notes User Interface: You must provide a user-friendly interface for the game. For C++, LISP and Prolog, ASCII graphics and command-line input are sufficient. For Java/Android project, graphical user interface is required. All human inputs must be validated. Before each player's turn, the following menu must be displayed and processed: Save the game Make a move Ask for help (only before human player plays) Quit the game The turn played by the computer as well as the strategy it uses must be displayed on the screen, e.g., The computer chose to play 5 of Spades because it could capture a triple stack with it.

The following must be displayed always on the screen: round number human hand, capture pile and score computer hand, capture pile and score layout the card at the top of stock pile - although it will be visible, assume that neither player can see it. At the end of each round, the points earned during that round as well as total points earned in the game by the two players must be declared. Help Mode: When the human player is playing, the computer must provide a help mode. If the human player asks for help, the computer must suggest: Which card the human player should play from their hand and why; What to capture with the card from the hand; What to capture with the card from the stock pile. The computer must use its own playing strategy to come up with its recommendation. It must print the rationale for its recommendation, e.g., I recommend you play Ace of Hearts from your hand to create a stacked pair.

Serialization: The user should be able to suspend the game before either player's turn, and resume at a later time from where the game was left off. In order to do this: Provide the option to serialize before each player's turn When the serialization option is exercised, your program should save the current state of the game into a file and quit. We will use text format for the file. The text format for C++/Java Android will be as follows: Round: 1

Computer: Score: 0 Hand: 1D 2D 4C KH 5D 6D XD 9S QS KS Capture Pile:

Human: Score: 0 Hand: JH 9S QS KD JC 1C 2C 7C KH 5H Capture Pile:

Layout: 6H XH JH 7D 8D 9D 4H 7H

Stock Pile: 7C 5C 6C XC 1H 2H 7H 8H 9H 1C 2C KC 1S 2S 7S QH 1D 2D 8C 9C QC 7D 1S 2S 1H 2H 4C 3S 4S 6D XD JD KS 5S 6S XS JS 3D 4D QD KD 5D 3C 3H 4H 8S KC 5C 6C XC JC 9C QC JD 5S 6S XS JS 3S 4S 8D 9D QD 3D 4D 8C 8H 9H QH 3H 3C 7S 8S 5H 6H XH

Next Player: Human The above snapshot is for the 1st round in the game. Each player has been dealt 10 cards and has a game score of 0. Neither player has any cards in Capture pile. Note that 10 is represented as X. Layout has been dealt 8 cards. Stock pile contains the remaining cards. The top of stock pile, i.e., the first card to be drawn from it is 7 of Clubs and not 10 of Hearts. (This order is very important!) Both the players have 2 Kings. Both have 1 Queen. Human has 1 Jack whereas computer has none. So, Human plays next (first). In Layout, a triple stack will be displayed hyphenated, e.g., 5C-5H-5D The text format for LISP will be as follows:

( ; Round: 1

; Computer Score: 0 ; Computer Hand: ( 1D 2D 4C KH 5D 6D XD 9S QS KS ) ; Computer Capture Pile: ()

; Human Score: 0 ; Human Hand: ( JH 9S QS KD JC 1C 2C 7C KH 5H ) ; Human Capture Pile: ()

; Layout: ( 6H XH JH 7D 8D 9D 4H 7H )

; Stock Pile: ( 7C 5C 6C XC 1H 2H 7H 8H 9H 1C 2C KC 1S 2S 7S QH 1D 2D 8C 9C QC 7D 1S 2S 1H 2H 4C 3S 4S 6D XD JD KS 5S 6S XS JS 3D 4D QD KD 5D 3C 3H 4H 8S KC 5C 6C XC JC 9C QC JD 5S 6S XS JS 3S 4S 8D 9D QD 3D 4D 8C 8H 9H QH 3H 3C 7S 8S 5H 6H XH )

; Next Player: Human ) Note that the comments above are for your convenience. You do not need to parse those - they will not appear in actual serialization files. In Layout, a triple stack will be displayed as a list, e.g., ( 5C 5H 5D ) The text format for Prolog will be as follows:

[ % Round: 1,

% Computer Score: 0, % Computer Hand: [ 1d, 2d, 4c, kh, 5d, 6d, xd, 9s, qs, ks ], % Computer Capture Pile: [],

% Human Score: 0, % Human Hand: [ jh, 9s, qs, kd, jc, 1c, 2c, 7c, kh, 5h ], % Human Capture Pile: [],

% Layout: [ 6h, xh, jh, 7d, 8d, 9d, 4h, 7h ],

% Stock Pile: [ 7c, 5c, 6c, xc, 1h, 2h, 7h, 8h, 9h, 1c, 2c, kc, 1s, 2s, 7s, qh, 1d, 2d, 8c, 9c, qc, 7d, 1s, 2s, 1h, 2h, 4c, 3s, 4s, 6d, xd, jd, ks, 5s, 6s, xs, js, 3d, 4d, qd, kd, 5d, 3c, 3h, 4h, 8s, kc, 5c, 6c, xc, jc, 9c, qc, jd, 5s, 6s, xs, js, 3s, 4s, 8d, 9d, qd, 3d, 4d, 8c, 8h, 9h, qh, 3h, 3c, 7s, 8s, 5h, 6h, xh ],

% Next Player: human ]. Note that the comments above are for your convenience. You do not need to parse those - they will not appear in actual serialization files. In Layout, a triple stack will be displayed as a list, e.g., [ 5c, 5h, 5d ] Important: The top card in stock pile - the only card that the player can play next, but cannot see, is the first card in the list (7c above).

When your program is started, it should provide the option to resume a game from a previously saved state. If yes, it should ask for the name of the text file from which to read the current state of the game, and resume playing from that state. Using any part of code available in textbooks or on the web is unacceptable.

Acknowledgments This game was adapted and modified from the description at gamerules.com
