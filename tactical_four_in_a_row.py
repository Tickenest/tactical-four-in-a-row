# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:30:36 2017

"""

from tkinter import *
import random
import copy

def findWin(table, winLength):

    #Assume that there's no winner
    gameOver = False
    
    #List to hold the coordinates for the winning pieces
    winCoords = []
    
    #Check whether there is any vertical win.  Basically, check every
    #possible location on the board where there could be a vertical win.
    #If the leftmost box to be tested has a piece, check whether enough pieces
    #to the right have enough of the same pieces to win.
    for row in range(0,len(table)-winLength+1):
        for col in range(0,len(table[0])):
            
            #matchPiece is either "X", "O", or " ".  If it's " ", then this
            #space cannot be the start of a winning combination.  Assume that
            #we have a win and then try to disprove it.
            matchPiece = table[row][col]
            foundWin = True
            
            #If the current space has a piece, then check the spaces to the
            #right to see if there's a winner
            if matchPiece in ["X","O"]:
                for x in range(1,winLength):
                    #As soon as we find a piece that doesn't match matchPiece,
                    #stop looking
                    if table[row+x][col] != matchPiece:
                        foundWin = False
                        break
                #If foundWin is true, then we didn't disprove a win, so
                #capture the winning coordinates
                if foundWin:
                    winCoords = []
                    for x in range(0,winLength):
                        winCoords.append([row+x,col])
            #If matchPiece is " ", then we didn't find a win
            else:
                foundWin = False
            #If we found a winner, print info about the win in the console and
            #set the gameOver variable to true, and then stop looking for a
            #winner
            if foundWin:
                print(str(winLength) + " in a column at {0},{1}".format(row,col))
                gameOver = True
                break
        if gameOver: break
    
    #If we haven't found a winner yet, keep looking
    if not gameOver:
        #Check whether there is any horizontal win.  Basically, check every
        #possible location on the board where there could be a horizontal win.
        #If the bottommost box to be tested has a piece, check whether enough
        #pieces above have enough of the same pieces to win.
        for col in range(0,len(table[0])-winLength+1):
            for row in range(0,len(table)):
                
                #matchPiece is either "X", "O", or " ".  If it's " ", then this
                #space cannot be the start of a winning combination.  Assume
                #that we have a win and then try to disprove it.
                matchPiece = table[row][col]
                foundWin = True
                
                #If the current space has a piece, then check the spaces above
                #to see if there's a winner    
                if matchPiece in ["X","O"]:
                    for x in range(1,winLength):
                        #As soon as we find a piece that doesn't match
                        #matchPiece, stop looking
                        if table[row][col+x] != matchPiece:
                            foundWin = False
                            break
                    #If foundWin is true, then we didn't disprove a win, so
                    #capture the winning coordinates
                    if foundWin:
                        winCoords = []
                        for x in range(0,winLength):
                            winCoords.append([row,col+x])
                #If matchPiece is " ", then we didn't find a win
                else:
                    foundWin = False
                #If we found a winner, print info about the win in the console
                #and set the gameOver variable to true, and then stop looking
                #for a winner
                if foundWin:
                    print(str(winLength) + " in a column at {0},{1}".format(row,col))
                    gameOver = True
                    break
            if gameOver: break

    #If we haven't found a winner yet, keep looking        
    if not gameOver:
        #Check whether there is any diagonal up-right win.  Basically, check
        #every possible location on the board where there could be a 
        #diagonal up-right win.  If the bottom-leftmost box to be tested has a
        #piece, check whether enough pieces up and right have enough of the
        #same pieces to win.
        for row in range(0,len(table)-winLength+1):
            for col in range(0,len(table[0])-winLength+1):
                
                #matchPiece is either "X", "O", or " ".  If it's " ", then this
                #space cannot be the start of a winning combination.  Assume
                #that we have a win and then try to disprove it.
                matchPiece = table[row][col]
                foundWin = True
                
                #If the current space has a piece, then check the spaces above
                #and to the right to see if there's a winner   
                if matchPiece in ["X","O"]:
                    for x in range(1,winLength):
                        #As soon as we find a piece that doesn't match
                        #matchPiece, stop looking
                        if table[row+x][col+x] != matchPiece:
                            foundWin = False
                            break
                    #If foundWin is true, then we didn't disprove a win, so
                    #capture the winning coordinates
                    if foundWin:
                        winCoords = []
                        for x in range(0,winLength):
                            winCoords.append([row+x,col+x])
                #If matchPiece is " ", then we didn't find a win
                else:
                    foundWin = False
                #If we found a winner, print info about the win in the console
                #and set the gameOver variable to true, and then stop looking
                #for a winner
                if foundWin:
                    print(str(winLength) + " diagonally up and right at {0},{1}".format(row,col))
                    gameOver = True
                    break
            if gameOver: break

    #If we haven't found a winner yet, keep looking    
    if not gameOver:
        #Check whether there is any diagonal up-left win.  Basically, check
        #every possible location on the board where there could be a 
        #diagonal up-left win.  If the bottom-rightmost box to be tested has a
        #piece, check whether enough pieces up and left have enough of the
        #same pieces to win.
        for row in range(winLength-1,len(table)):
            for col in range(0,len(table[0])-winLength+1):
                
                #matchPiece is either "X", "O", or " ".  If it's " ", then this
                #space cannot be the start of a winning combination.  Assume
                #that we have a win and then try to disprove it.
                matchPiece = table[row][col]
                foundWin = True
                
                #If the current space has a piece, then check the spaces above
                #and to the left to see if there's a winner  
                if matchPiece in ["X","O"]:
                    for x in range(1,winLength):
                        #As soon as we find a piece that doesn't match
                        #matchPiece, stop looking
                        if table[row-x][col+x] != matchPiece:
                            foundWin = False
                            break
                    #If foundWin is true, then we didn't disprove a win, so
                    #capture the winning coordinates
                    if foundWin:
                        winCoords = []
                        for x in range(0,winLength):
                            winCoords.append([row-x,col+x])
                #If matchPiece is " ", then we didn't find a win
                else:
                    foundWin = False
                #If we found a winner, print info about the win in the console
                #and set the gameOver variable to true, and then stop looking
                #for a winner
                if foundWin:
                    print(str(winLength) + " diagonally up and left at {0},{1}".format(row,col))
                    gameOver = True
                    break
            if gameOver: break
        
    #Return whether the game is over, whether there's actually a winner, and
    #the win coordinates
    return(gameOver, foundWin, winCoords)
    
def placePiece(inTable, placeCol, whoseTurn):

    #Make a deepcopy of inTable so that we don't modify the input list of lists
    curTable = copy.deepcopy(inTable)
    
    #Assume we can't place a piece
    placedPiece = False

    #Place the piece if possible by finding the lowest empty space in the
    #chosen column
    for count in range(0,len(curTable)):
        if curTable[count][placeCol] not in ["X","O"]:
            placedPiece = True
            #Place a "X" for player 1 or a "O" for player 2
            if whoseTurn == 1:
                curTable[count][placeCol] = "X"
            else:
                curTable[count][placeCol] = "O"
            break
        
    return[curTable, placedPiece]
    
def chooseCard(table, playerCards, opponentCards, winLength, lastCol,
               whoseTurn, helpHurtHowMuch):
    
    print(helpHurtHowMuch)
    
    #Computer algorithm isn't quite done yet, so just choose "random"
    #nastyNiceOrRandom = "random"
    
    #If we're doing a random draw, just pick the card here and return
    if helpHurtHowMuch == "random":
        return (random.sample(playerCards, 1))
    
    #Get the set of all possible combinations that could be made in the
    #next turn
    allSums = {}

    for x in opponentCards:
        for y in playerCards:
            allSums[x+y] = 0
    
    #For each entry in allSums, classify it as 1 if it allows self.nwin
    #in a row to be formed, 2 if it allows self.nwin-1 in a row to be
    #formed, 3 if it lands in the center or center two columns, and 4
    #otherwise.
    
    #The trick is that the priority order changes depending upon whether we're
    #being nice or nasty.  If we're being nasty, then we want a number to be
    #classified with the lowest number possible because we're trying to avoid
    #the outcomes that are most helpful to the opponent.  If we're being nice,
    #the opposite is true and we want to classify each number with the highest
    #number possible because we're trying to avoid the outcomes that are most
    #harmful to the opponent.
    
    #So if we're being nasty, a number that could be classified as 1, 2, and 4
    #should be classified as 1 because we care most about the fact that
    #choosing that number could cause us to lose.  However, if we're being
    #nice, we would classify that same number as 4 because it could cause the
    #least desirable outcome and we'd prefer to pick a number that would avoid
    #that outcome.
    
    #Determine the middle column(s)
    if len(table[0]) % 2 == 0:
        midCols = [int(len(table[0])/2),
          int(len(table[0])/2-1)]
    else: midCols = [int(len(table[0])/2)]
    
    #List to hold all of the classifications that the current sum could be
    #given
    for num in allSums:
        possibleNumberClasses = []
    
        #Test whether the current number could result in the next piece
        #landing in a middle column
        if (lastCol + num) % len(table[0]) in midCols:
            possibleNumberClasses.append(3)
            
        #Now test each number in allSums to see if a winLength-in-a-row or a
        #(winLength-1)-in-a-row forms if that number is used to add a piece to
        #the table.  Classify the number as 1 or 2, depending.
        testTable, _ = placePiece(table, (lastCol+num) % len(table[0]),
                                  whoseTurn)
        _, foundTestWin, _ = findWin(testTable, winLength)
        if foundTestWin:
            possibleNumberClasses.append(1)
        else:
            _, foundTestWin, _ = findWin(testTable, winLength-1)
            if foundTestWin:
                possibleNumberClasses.append(2)
                
        #Now that we've determined into which classes the current sum could be
        #placed, determine its final classification depending upon whether
        #we're being nasty or nice.  If possibleNumberClasses is empty, then
        #the classification must be 4.  Otherwise, get the maximum number if
        #we're trying to hurt the current player or the minimum number if we're
        #trying to help the current player.
        if len(possibleNumberClasses) == 0:
            allSums[num] = 4
        else:
            if helpHurtHowMuch in ["hurtmost", "hurtleast"]:
                allSums[num] = max(possibleNumberClasses)
            else:
                allSums[num] = min(possibleNumberClasses)
    print(allSums)
            
    #Classify each of the playerCards.  If we're trying to hurt the current
    #player the most or help the current player the least, choose the maximum
    #class of all the possible sums for that card.  If we're trying to help
    #the current player the most or hurt the current player the least, choose
    #the minimum class of all the possible sums for that card.
    playerCardsDict = {}
    for x in playerCards:
        for y in opponentCards:
            curSum = x + y
            if x in playerCardsDict:
                if helpHurtHowMuch in ["hurtmost", "hurtleast"]:
                    playerCardsDict[x] = max(playerCardsDict[x],
                                   allSums[curSum]) 
                else:
                    playerCardsDict[x] = min(playerCardsDict[x],
                                   allSums[curSum])
            else:
                playerCardsDict[x] = allSums[curSum]
    print(playerCardsDict)
    print("---")
            
    #Now choose the next card
    
    #If we're hurting the current player the most or helping the current player
    #the least, choose the lowest valued card in playerCardsDict.  If we're
    #hurting the current player the least or helping the current player the
    #most, choose the highest valued card in playerCardsDict.  If there's a
    #tie, choose one of the tied cards at random.
    goodCardsList = []
    if helpHurtHowMuch in ["hurtleast", "helpmost"]:
        #Get the lowest class that appears in the playerCardsDict values
        bestRank = playerCardsDict[min(playerCardsDict,
                                       key=playerCardsDict.get)]
        print("bestRank = " + str(bestRank))
        #Get the keys (cards) in playerCardsDict that have bestRank as their
        #value
        for card, value in playerCardsDict.items():
            if value == bestRank:
                goodCardsList.append(card)
    else:
        #Get the highest class that appears in the playerCardsDict values
        bestRank = playerCardsDict[max(playerCardsDict,
                                       key=playerCardsDict.get)]
        print("bestRank = " + str(bestRank))
        #Get the keys (cards) in playerCardsDict that have bestRank as their
        #value
        for card, value in playerCardsDict.items():
            if value == bestRank:
                goodCardsList.append(card)
        
    #Now choose any card in goodCardsList
    return (random.sample(goodCardsList,1)[0])

def calcCircleCoords(ulBoxX, ulBoxY, boxSideLength, diameterLengthFactor):
    
    '''diameterLengthFactor should be a real number between 0 and 1'''
    
    distIn = boxSideLength * (1 - diameterLengthFactor) / 2
    ulX = ulBoxX + distIn
    ulY = ulBoxY + distIn
    brX = ulBoxX + boxSideLength - distIn
    brY = ulBoxY + boxSideLength - distIn
    
    return (ulX, ulY, brX, brY)

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master, background="#B3B3B3")
        self.master = master
        self.init_window()
        
    def initialize(self):
    
        #Create a blank list to hold the board information
        self.table = []
    
        #Fill each entry with a string with a single space
        for rcount in range(0,self.nrow):
            self.table.append([" "]*self.ncol)
            
        #Create the lists of both players' cards
        self.p1Cards = list(range(self.minCard, self.maxCard+1))
        self.p2Cards = list(range(self.minCard, self.maxCard+1))
        
        #Set the last column, turn count, and whose turn it is variables
        self.lastCol = 0
        self.turnCount = 0
        self.whoseTurn = 1
        
    def endGame(self, canvasBottom, canvasTop, canvasLeft, canvasRight,
                winCoords):
        
        #Wrap everything up if the game is over
        
        #If there was an actual winner...
        if self.foundWin:
            
            #Calculate the height and width of each rectangle in order to maximize
            #the canvas space that the game board will fill.  Remember that we need
            #to calculate as if there's an extra row on top of the board to hold
            #the lastCol marker.
            rowsNeeded = self.nrow+1
            colsNeeded = self.ncol
            
            #Calculate how big each square would be if we fill the space east-west.
            #Then see if that will occupy too much space north-south.  If it does,
            #then we have to use the north-south information to set the square
            #size.
            testSquareWidth = int((canvasRight-canvasLeft)/colsNeeded)
            if testSquareWidth * rowsNeeded <= canvasBottom - canvasTop:
                squareWidth = testSquareWidth
            else:
                squareWidth = int((canvasBottom-canvasTop)/rowsNeeded)
            
            #Announce the winner
            self.announceWinText = Label(self,
                                         text="GAME OVER!  PLAYER {0} WINS!".format(str(self.whoseTurn)),
                                         justify="left", background="#B3B3B3")
            self.announceWinText.place(x=122,y=635)
            print(self.winCoords)
            
            #Color the winning pieces in a gold outline
            for i in range(0,self.nwin):
                xUL, yUL, xBR, yBR = calcCircleCoords(self.canvasLeft+winCoords[i][1]*squareWidth,
                                                      self.canvasBottom-(winCoords[i][0]+1)*squareWidth,
                                                      squareWidth, 0.67)
#                xUL = 12+self.winCoords[i][1]*60
#                yUL = self.tableBottom-50-self.winCoords[i][0]*60
#                xBR = 52+self.winCoords[i][1]*60
#                yBR = self.tableBottom-10-self.winCoords[i][0]*60
                print([xUL,yUL,xBR,yBR])
                self.tableCanvas.create_oval(xUL, yUL, xBR, yBR, fill="",
                                             outline="#FFFF00", width=10)                
            
        #If there was no winner...
        else:
            #Announce the stalemate
            self.announceWinText = Label(self,
                                         text="GAME OVER!  NOBODY WINS!".format(str(self.whoseTurn)),
                                         justify="left", background="#B3B3B3")
            self.announceWinText.place(x=122,y=635)
            
        #Disable the card entry methods so that the player doesn't keep adding
        #pieces
        self.p1CardEntry['state'] = 'disabled'
        self.p1CardEntry.unbind("<Return>")
        self.p1CardButton['state'] = 'disabled'

    def checkTable(self):  
        
        #Check the status of the current game board
        self.gameOver, self.foundWin, self.winCoords = findWin(self.table,
                                                               self.nwin)
                
        #End the game if the board is full
        if not any(" " in row for row in self.table):
            self.gameOver = True
        
    def doTurn(self):
        
        #Figure out whose turn it is
        if self.turnCount % 8 in [0,2,5,7]:
            self.whoseTurn = 1
        else: self.whoseTurn = 2
    
        #If there's a human player, get whatever the human player typed into
        #the card entry box
        print(self.nplayers)
        if self.nplayers == 0:
            if len(self.p1Cards) == 1:
                p1Card = self.p1Cards[0]
            else:
                if self.whoseTurn == 1:
                    chooseType = "helpmost"
                else:
                    chooseType = "helpleast"
                p1Card = chooseCard(self.table, self.p1Cards, self.p2Cards,
                                    self.nwin, self.lastCol, self.whoseTurn,
                                    chooseType)
        else:
            p1Card = self.p1CardEntry.get()
        
        #Clear any previous "Invalid card!" message and then see if the user
        #entered a valid card
        try:
            if int(p1Card) in self.p1Cards:
                self.invalidCardText = Label(self, text=" "*200,
                                             justify="left",
                                             background="#B3B3B3")
                self.invalidCardText.place(x=440,y=740)
            else:
                self.invalidCardText = Label(self, text="Invalid card!",
                                             justify="left",
                                             background="#B3B3B3")
                self.invalidCardText.place(x=440,y=740)
                #If the card was invalid, then escape from this procedure
                return            
        #An exception would be caused if the user enters something other than
        #a number in the box
        except:
            self.invalidCardText = Label(self, text="Invalid card!",
                             justify="left",
                             background="#B3B3B3")
            self.invalidCardText.place(x=440,y=740)
            #If the card was invalid, then escape from this procedure
            return
        
        #Don't bother with the choosing algorithm if there's only one card left
        #in player 2's hand
        if len(self.p2Cards) == 1:
            p2Card = self.p2Cards[0]
        else:        
            if self.whoseTurn == 1:
                chooseType = "helpleast"
            else:
                chooseType = "helpmost"
            p2Card = chooseCard(self.table, self.p2Cards, self.p1Cards,
                                self.nwin, self.lastCol, self.whoseTurn,
                                chooseType)
        
        #Show what card the player chose
        self.p1CardEntryText = Label(self, text="Player 1 chose " + str(p1Card),
                                     justify="left", background="#B3B3B3")
        self.p1CardEntryText.place(x=300,y=720)
        
        #Show what card the computer chose
        self.p2CardEntryText = Label(self, text="Player 2 chose " + str(p2Card),
                                     justify="left", background="#B3B3B3")
        self.p2CardEntryText.place(x=300,y=740)
        
        #Remove the chosen cards from the players' hands
        self.p1Cards.remove(int(p1Card))
        self.p2Cards.remove(p2Card)
    
        #Update self.lastCol with the location of the next piece to be played
        self.lastCol = (self.lastCol + int(p1Card) + int(p2Card)) % len(self.table[0])
    
        #Try to place the current piece
        self.table, placedPiece = placePiece(self.table, self.lastCol,
                                             self.whoseTurn)
        
        #If the column was full, say so
        if not placedPiece:
            self.placedPieceText = Label(self,
                                         text="Can't place a piece in column {0}!".format(self.lastCol),
                                         justify="left", background="#B3B3B3")
        #Otherwise, blow away any previous text about an unplaced piece
        else:
            self.placedPieceText = Label(self, text=" "*200, justify="left",
                                         background="#B3B3B3")
        self.placedPieceText.place(x=420,y=720)
    
        #Check whether the game is over or not (because there's a winner or
        #the table is full)
        self.checkTable()
    
        #If all of the cards are used up, replenish both hands
        if len(self.p1Cards) == 0:
            self.p1Cards = list(range(self.minCard, self.maxCard+1))
            self.p2Cards = list(range(self.minCard, self.maxCard+1))
        
        #Increment the turn count
        self.turnCount += 1
        
        #Draw the updated table only if there are human players
        if self.drawGameBool.get() != 0:
            self.drawTable(self.canvasBottom, self.canvasTop, self.canvasLeft,
                           self.canvasRight)
        
        #Set the focus back to the entry box
        self.p1CardEntry.focus_set()
        
        #Refresh the display
        self.tableCanvas.update_idletasks()
            
        #Take care of things if the game is over
        if self.gameOver:
            self.drawTable(self.canvasBottom, self.canvasTop, self.canvasLeft,
                           self.canvasRight)
            self.endGame(self.canvasBottom, self.canvasTop, self.canvasLeft,
                       self.canvasRight, self.winCoords)
        
    def drawTable(self, canvasBottom, canvasTop, canvasLeft, canvasRight):
        
        #Because the whole board layout (including the squares) gets drawn from
        #scratch each time, just delete all the existing drawn shapes so that
        #tkinter doesn't get bogged down with all of those existing items
        self.tableCanvas.delete(ALL)
        
        #Calculate the height and width of each rectangle in order to maximize
        #the canvas space that the game board will fill.  Remember that we need
        #to calculate as if there's an extra row on top of the board to hold
        #the lastCol marker.
        rowsNeeded = self.nrow+1
        colsNeeded = self.ncol
        
        #Calculate how big each square would be if we fill the space east-west.
        #Then see if that will occupy too much space north-south.  If it does,
        #then we have to use the north-south information to set the square
        #size.
        testSquareWidth = int((canvasRight-canvasLeft)/colsNeeded)
        if testSquareWidth * rowsNeeded <= canvasBottom - canvasTop:
            squareWidth = testSquareWidth
        else:
            squareWidth = int((canvasBottom-canvasTop)/rowsNeeded)
            
        #Draw the board for the dimensions of the current game
        
        #Calculate the canvas coordinates of the top of the marker row        
        markerRowTop = canvasBottom - squareWidth * rowsNeeded
        
        #Draw the marker above the board to indicate where the last piece was
        #played and whose turn it is
        if self.turnCount % 8 in [0,2,5,7]: markerFill = "red"
        else: markerFill = "black"
        xUL, yUL, xBR, yBR = calcCircleCoords(canvasLeft+squareWidth*self.lastCol,
                                              markerRowTop,
                                              squareWidth,
                                              0.67)
        self.tableCanvas.create_oval(xUL, yUL, xBR, yBR, fill=markerFill)
        
        #Draw the board squares
        for y in range(0,self.nrow):
            for x in range(0,self.ncol):
                self.tableCanvas.create_rectangle(canvasLeft+squareWidth*x,
                                                  canvasBottom-squareWidth*(y+1),
                                                  canvasLeft+squareWidth*(x+1),
                                                  canvasBottom-squareWidth*y,
                                                  fill="#B3B3B3",
                                                  outline="black")
                
        #Draw all of the pieces from bottom to top (from large number
        #coordinates to small number coordinates)
        for y in range(0,self.nrow):
            for x in range(0,self.ncol):
                fillColor = "#B3B3B3"
                outlineColor = "#B3B3B3"
                #Draw a red piece for player 1 and a black piece for player 2
                if self.table[y][x] == "X":
                    fillColor = "red"
                    outlineColor = "black"
                elif self.table[y][x] == "O":
                    fillColor = "black"
                    outlineColor = "black"
                xUL, yUL, xBR, yBR = calcCircleCoords(canvasLeft+squareWidth*x,
                                                      canvasBottom-squareWidth*(y+1),
                                                      squareWidth, 0.67)
                self.tableCanvas.create_oval(xUL, yUL, xBR, yBR,
                                             fill=fillColor,
                                             outline=outlineColor)
        
        #Create/update a bunch of text and other widgets
        self.p1CardsText = Label(self, text=" "*200,
                                 justify="left", background="#B3B3B3")
        self.p1CardsText.place(x=120, y=668)
        self.p1CardsText = Label(self, text="Player 1 Cards: "+str(self.p1Cards),
                                 justify="left", background="#B3B3B3",
                                 font=("Helvetica",12))
        self.p1CardsText.place(x=120, y=668)
        
        self.p2CardsText = Label(self, text=" "*200,
                                 justify="left", background="#B3B3B3")
        self.p2CardsText.place(x=120, y=688)
        self.p2CardsText = Label(self, text="Player 2 Cards: "+str(self.p2Cards),
                                 justify="left", background="#B3B3B3",
                                 font=("Helvetica",12))
        self.p2CardsText.place(x=120, y=688)
        
        self.p1CardEntryText = Label(self, text="Your card:", justify="right",
                                     background="#B3B3B3")
        self.p1CardEntryText.place(x=120,y=718)
        
        self.p1CardEntry = Entry(self, width=5)
        self.p1CardEntry.place(x=180,y=720)
        #The .bind method allows the player to press Enter when the focus is
        #on the card entry box instead of having to click on the buttom
        self.p1CardEntry.bind("<Return>", lambda e: self.doTurn())
        #If there's only 1 card left in the hand, add it to the box for the
        #user's convenience
        if len(self.p1Cards) == 1:
            self.p1CardEntry.insert(0,self.p1Cards[0])
        
        self.p1CardButton = Button(self, text="Play Card",
                                   background="#B3B3B3", command=self.doTurn)
        self.p1CardButton.place(x=220,y=720)
        
    def startGame(self):
        
        #Make sure that the user entered a win length of at least 2
        goodWin = False
        while not goodWin:
            try:                
                self.nwin = int(self.nWinEntry.get())
                if self.nwin >= 2:
                    goodWin = True
                else: print("ERROR: Invalid win length!")
            except:
                print("ERROR: Invalid win length!")

        #Make sure the user didn't enter a number of rows or columns that's
        #less than the number in a row needed to win
        goodRows = False
        while not goodRows:
            try:
                self.nrow = int(self.nRowsEntry.get())
                if self.nrow < self.nwin: print("ERROR: Invalid number of rows!")
                else: goodRows = True
            except:
                print("ERROR: Invalid number of rows!")
                
        goodCols = False
        while not goodCols:
            try:
                self.ncol = int(self.nColsEntry.get())
                if self.ncol < self.nwin: print("ERROR: Invalid number of columns!")
                else: goodCols = True
            except:
                print("ERROR: Invalid number of columns!")
    
        #Make sure that the user entered a valid smallest card (at least 0)
        goodCardsMin = False
        while not goodCardsMin:
            try:
                self.minCard = int(self.minCardEntry.get())
                if 0 <= self.minCard:
                    goodCardsMin = True
                else: print("ERROR: Invalid minimum card number!")
            except:
                print("ERROR: Invalid minimum card number!")
                
        #Make sure the user entered a valid largest card (at least as large
        #as the smallest card)
        goodCardsMax = False
        while not goodCardsMax:
            try:
                self.maxCard = int(self.maxCardEntry.get())
                if self.maxCard >= self.minCard:
                    goodCardsMax = True
                else: print("ERROR: Invalid maximum card number!")
            except:
                print("ERROR: Invalid maximum card number!")
                
        #Set up a bunch of variables
        self.initialize()
        
        #Set the coordinates of the canvas extremes
        self.canvasTop = 2
        self.canvasBottom = 616
        self.canvasLeft = 2
        self.canvasRight = 898
        
        #Draw the initial table
        self.drawTable(self.canvasBottom, self.canvasTop, self.canvasLeft,
                       self.canvasRight)
        
        #The game can't possibly be over before it begins!
        self.gameOver = False
        
        #Set the focus to the entry box
        self.p1CardEntry.focus_set()
        
        #If the numbers of players is zero, then have the computer play things
        #out at this point
        self.nplayers = int(self.nPlayersEntry.get())
        if self.nplayers == 0:
            while not self.gameOver:
                self.doTurn()
        

                   
        
    def init_window(self):
        
        #Setup a bunch of variables and widgets
        self.title = "Tactical Four in a Row"
        
        self.pack(fill=BOTH, expand=1)
        
        self.drawGameQuestion = Label(self, text="Draw game?", justify="right",
                                      background="#B3B3B3")
        self.drawGameQuestion.place(x=14, y=520)
        
        self.drawGameBool = IntVar()
        self.drawGameChkBox = Checkbutton(self, text="", background="#B3B3B3",
                                          variable=self.drawGameBool)
        self.drawGameChkBox.place(x=84, y=520)
        
        self.nPlayersQuestion = Label(self, text="# of players:",
                                      justify="right", background="#B3B3B3")
        self.nPlayersQuestion.place(x=14, y=548)
        
        self.nPlayersEntry = Entry(self, width=2)
        self.nPlayersEntry.insert(0,"1")
        self.nPlayersEntry.place(x=87, y=548)

        self.nRowsQuestion = Label(self, text="# of rows:", justify="right",
                                   background="#B3B3B3")
        self.nRowsQuestion.place(x=26, y=568)
        
        self.nRowsEntry = Entry(self, width=2)
        self.nRowsEntry.insert(0,"6")
        self.nRowsEntry.place(x=87, y=568)
        
        self.nColsQuestion = Label(self, text="# of columns:", justify="right",
                                   background="#B3B3B3")
        self.nColsQuestion.place(x=5, y=588)
        
        self.nColsEntry = Entry(self, width=2)
        self.nColsEntry.insert(0,"7")
        self.nColsEntry.place(x=87, y=590)
        
        self.nWinQuestion = Label(self, text="# in a row\nto win:",
                                  justify="right", background="#B3B3B3")
        self.nWinQuestion.place(x=26, y=608)
        
        self.nWinEntry = Entry(self, width=2)
        self.nWinEntry.insert(0,"2")
        self.nWinEntry.place(x=87, y=618)
        
        self.minCardQuestion = Label(self, text="Min card:", justify="right",
                                     background="#B3B3B3")
        self.minCardQuestion.place(x=28, y=648)
        
        self.minCardEntry = Entry(self, width=2)
        self.minCardEntry.insert(0,"0")
        self.minCardEntry.place(x=87,y=650)
        
        self.maxCardQuestion = Label(self, text="Max card:", justify="right",
                                     background="#B3B3B3")
        self.maxCardQuestion.place(x=28, y=668)
        
        self.maxCardEntry = Entry(self, width=2)
        self.maxCardEntry.insert(0,"3")
        self.maxCardEntry.place(x=87,y=670)
        
        self.newGameButton = Button(self, text="Start\nNew Game",
                               command=self.startGame, background="#B3B3B3")
        self.newGameButton.place(x=22,y=710)
        
        self.tableCanvas = Canvas(self, width=900, height=618,
                                  background="#B3B3B3", bd=0,
                                  highlightthickness=1)
        self.tableCanvas.place(x=120,y=2)
        
        self.announceWinText = Label(self, text=" "*200, justify="left",
                                     background="#B3B3B3")
        self.announceWinText.place(x=122,y=635)
                


root = Tk()

root.geometry("1024x768")
root.title("Tactical Four in a Row")
app = Application(root)
root.mainloop()