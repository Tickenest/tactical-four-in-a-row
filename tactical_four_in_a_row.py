# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:30:36 2017

"""

from tkinter import *
import random
import copy

def getRowFromPiece(table, xCoord, yCoord, winLength, direction):
    
    '''Returns a list of the like pieces and empty spaces that emanate from
    a given piece at position xCoord, yCoord in table in the specified
    direction.  direction can be "h" for horizontal, "v" for vertical,
    "ur" for diagonally up and right, and "ul" for diagonally up and left.
    
    The emanation stops when it hits either a piece that's different from the
    piece at xCoord, yCoord or hits the edge of the game board.
    
    Returns a list of two lists.  The first list is the emanation behind (left,
    down, down-left or down-right, depending upon the value of direction) 
    xCoord, yCoord and the second list is the emanation in front.  Note that
    the space representing xCoord, yCoord is NOT returned as part of the
    output.'''

    #checkSpaces will be a list of two lists.  It will contain the contiguous
    #open spaces and/or like pieces extending from the placed piece until that
    #radiating hits either an opponent's piece or a wall.  The first list will
    #hold the pieces/spaces emanating "backwards" from the placed piece and the
    #second list will contain those emanating "forwards".
    checkSpaces = [[],[]]

    #Get the piece that's just been placed
    placedPiece = table[yCoord][xCoord]
#    print("xCoord: " + str(xCoord))
#    print("yCoord: " + str(yCoord))
#    print("placedPiece: " + placedPiece)
    
    if direction == "h":
        #Check the horizontal direction, starting by going left from the placed
        #piece
        for i in range(xCoord-1, xCoord-winLength, -1):
            if i >= 0:
                if table[yCoord][i] in [" ", placedPiece]:
                    #If the current position either has a piece that's the same
                    #as the placed piece or is empty, append it to checkSpaces
                    checkSpaces[0].append(table[yCoord][i])
                else:
                    #If the current position has an opposing piece then stop
                    #searching
                    break
            else:
                #If we've hit the table boundary, stop searching
                break
            
        #Now check to the right
        for i in range(xCoord+1, xCoord+winLength):
            if i < len(table[0]):
                if table[yCoord][i] in [" ", placedPiece]:
                    #If the current position either has a piece that's the same
                    #as the placed piece or is empty, append it to checkSpaces
                    checkSpaces[1].append(table[yCoord][i])
                else:
                    #If the current position has an opposing piece then stop
                    #searching
                    break
            else:
                #If we've hit the table boundary, stop searching
                break
        
    if direction == "v":
        
        #Check the vertical direction, starting by going down from the placed
        #piece
        for i in range(yCoord-1, yCoord-winLength, -1):
            if i >= 0:
                if table[i][xCoord] in [" ", placedPiece]:
                    #If the current position either has a piece that's the same
                    #as the placed piece or is empty, append it to checkSpaces
                    checkSpaces[0].append(table[i][xCoord])
                else:
                    #If the current position has an opposing piece then stop
                    #searching
                    break
            else:
                #If we've hit the table boundary, stop searching
                break
            
        #Now check going up
        for i in range(yCoord+1, yCoord+winLength):
            if i < len(table):
                if table[i][xCoord] in [" ", placedPiece]:
                    #If the current position either has a piece that's the same
                    #as the placed piece or is empty, append it to checkSpaces
                    checkSpaces[1].append(table[i][xCoord])
                else:
                    #If the current position has an opposing piece then stop
                    #searching
                    break
            else:
                #If we've hit the table boundary, stop searching
                break
            
    if direction == "ur":
            
        #Check the diagonally up and right direction, starting by searching
        #down and left
        for i in range(1, winLength):
            if yCoord-i >= 0 and xCoord-i >= 0:
                if table[yCoord-i][xCoord-i] in [" ", placedPiece]:
                    #If the current position either has a piece that's the same
                    #as the placed piece or is empty, append it to checkSpaces
                    checkSpaces[0].append(table[yCoord-i][xCoord-i])
            else:
                #If the current position has an opposing piece or if i is less
                #than 0, then we've hit one kind of barrier or another so stop
                #searching
                break
            
        #Now search up and right
        for i in range(1, winLength):
            if yCoord+i < len(table) and xCoord+i < len(table[0]):
                if table[yCoord+i][xCoord+i] in [" ", placedPiece]:
                    #If the current position either has a piece that's the same
                    #as the placed piece or is empty, append it to checkSpaces
                    checkSpaces[1].append(table[yCoord+i][xCoord+i])
            else:
                #If the current position has an opposing piece or if i is less
                #than 0, then we've hit one kind of barrier or another so stop
                #searching
                break
            
    if direction == "ul":
            
        #Check the diagonally up and left direction, starting by searching down
        #and right
        for i in range(1, winLength):
            if yCoord-i >= 0 and xCoord+i < len(table[0]):
                if table[yCoord-i][xCoord+i] in [" ", placedPiece]:
                    #If the current position either has a piece that's the same
                    #as the placed piece or is empty, append it to checkSpaces
#                    print("yCoord-i: " + str(yCoord-i))
#                    print("xCoord+i: " + str(xCoord+i))
#                    print(table[yCoord-i][xCoord+i])
                    checkSpaces[0].append(table[yCoord-i][xCoord+i])
                else:
                    break
            else:
                #If the current position has an opposing piece or if i is less
                #than 0, then we've hit one kind of barrier or another so stop
                #searching
                break
            
        #Now search up and left
        for i in range(1, winLength):
            if yCoord+i < len(table) and xCoord-i >= 0:
                if table[yCoord+i][xCoord-i] in [" ", placedPiece]:
                    #If the current position either has a piece that's the same
                    #as the placed piece or is empty, append it to checkSpaces
                    checkSpaces[1].append(table[yCoord+i][xCoord-i])
                else:
                    break
            else:
                #If the current position has an opposing piece or if i is less
                #than 0, then we've hit one kind of barrier or another so stop
                #searching
                break
            
    return(checkSpaces)

def calcRowValue(inRows, winLength):
    
    '''Calculate the value of a list containing the like pieces and blank
    spaces emanating from where the latest piece in table was placed.
    
    inRows is two lists.  The first list is the pieces and spaces emanating
    from behind/below the piece in order emanating from the piece.  The second
    list is the pieces and spaces emanating from ahead of/in front of the piece
    in order emanating from the piece.  For example, if winLength is 4, we're
    testing a set of horizontal spaces, and the spaces we're testing are:
        
    [" ", "X", "*", " ", " ", "X"]
    
    and the "*" is the position of the placed piece, then inRows should be

    [["X", " "],[" ", " ", "X"]]
    
    Note that inRows[0] is the REVERSE of the order of the spaces in the
    original game board.  Here is how inRows would be scored:
    
    inRows[0][0] ("X") is worth winLength-1 points: 3
    inRows[0][1] (" ") is worth winLength-2*0.5 points: 1
    inRows[1][0] (" ") is worth winLength-1*0.5 points: 1.5
    inRows[1][1] (" ") is worth winLength-2*0.5 points: 1
    inRows[1][2] ("X") is worth winLength-3 points: 1
    
    The value of an empty space is half that of a piece in the same position.
    
    The total value of inRows would be 3 + 1 + 1.5 + 1 + 1 = 7.5 and that
    value is returned by the function.
    '''
    
    #First, check whether the lengths of the two inRows lists combined is
    #at least as long as winLength-1, because if it isn't then the placed
    #piece cannot possibly contribute to a win in the current direction, so
    #give it a score of 0
    if len(inRows[0]) + len(inRows[1]) < winLength - 1:
        return (0)
    
    #Otherwise, score the row. The method is to score the pieces that are
    #closer to the placed piece higher than those that are far away. Empty
    #spaces are worth half as much as occupied spaces.
    
    #Start the scoring at 0
    score = 0
    
    for squareSets in inRows:
        #Start the value of the potential pieces at winLength - 1, and
        #lower it by 1 for each square we process because each square is
        #far away from the placed piece than the one that preceded it.  A
        #piece that's the maximum distance away scores 1 by this system.
        curValue = winLength - 1
        for square in squareSets:
            if square != " ":
                score += curValue
            else:
                score += curValue/2
            #Decrement curValue by 1 regardless of whether square was a
            #piece or a space
            curValue -= 1
            
    return (score)

def calcPlacementValue(table, xCoord, yCoord, winLength):
    
    '''Calculates the value of placing a piece at xCoord, yCoord in table.
    
    To calculate the value, run getRowFromPiece to calculate the values of the
    "emanated" rows from xCoord, yCoord (see the description of getRowFromPiece
    for more info on how the "emanated" rows are calculated) in the horizontal,
    vertical, and diagonal directions.  Then just add all the scores together
    and return that sum.'''
    
    #Keep track of the placed piece's running score as we evaluate it
    score = 0
    
    #Get the score for each direction and add it to the running tally
    score += calcRowValue(getRowFromPiece(table, xCoord, yCoord, winLength, "h"),
                          winLength)
    
    score += calcRowValue(getRowFromPiece(table, xCoord, yCoord, winLength, "v"),
                          winLength)
    
    score += calcRowValue(getRowFromPiece(table, xCoord, yCoord, winLength, "ur"),
                          winLength)
    
    score += calcRowValue(getRowFromPiece(table, xCoord, yCoord, winLength, "ul"),
                          winLength)
    
    #Return the final score
    return (score)

def findWinCurPiece(table, xCoord, yCoord, winLength):
    
    '''Discovers if there is a win going through the piece at xCoord, yCoord.
    
    Returns True if there is a win and False if there is not a win.
    '''
    
    #Look in each direction for a win: horizontal, vertical, diagonally up and
    #right, and diagonally up and left
    for direction in ("h", "v", "ur", "ul"):
        #Get the row that extends in the chosen direction from xCoord, yCoord
        checkRow = getRowFromPiece(table, xCoord, yCoord, winLength, direction)
#        print(checkRow)
        #Calculate the coordinate of the very first space in checkRow and the
        #coordinate of the very last space in checkRow.
        if direction == "h":
            xCoordStart = xCoord - len(checkRow[0])
            yCoordStart = yCoord
        elif direction == "v":
            xCoordStart = xCoord
            yCoordStart = yCoord - len(checkRow[0])
        elif direction == "ur":
            xCoordStart = xCoord - len(checkRow[0])
            yCoordStart = yCoord - len(checkRow[0])
        else:
            xCoordStart = xCoord + len(checkRow[0])
            yCoordStart = yCoord - len(checkRow[0])
        
        #Reverse checkRow[0] because it lists the pieces in order eminating
        #backwards from the placed piece, which is the opposite of what we want
        checkRow[0].reverse()
        #Because checkRow is two separate lists, we have to build the final
        #row to check
        checkRow = checkRow[0] + [table[yCoord][xCoord]] + checkRow[1]
        #Count how many consecutive pieces in a row that are found.
        piecesInARow = 0
        #Check each piece in checkRow in order
        count = 0
        winCoords = []
        while count < len(checkRow):
            if checkRow[count] != " ":
                #If the current entry isn't a space, then we're one piece
                #closer to finding a win
                piecesInARow += 1
                if direction == "h":
                    winCoords.append([yCoordStart,xCoordStart+count])
                elif direction == "v":
                    winCoords.append([yCoordStart+count,xCoordStart])
                elif direction == "ur":
                    winCoords.append([yCoordStart+count,xCoordStart+count])
                else:
                    winCoords.append([yCoordStart+count,xCoordStart-count])
                #If we've got enough in a row to win, return True, indicating
                #that we've found a win (and we can stop searching), as well as
                #the winCoords.
                if piecesInARow == winLength:
                    return (True, winCoords)
            else:
                #If the current entry is a space, then we have to start over
                #looking for a win
                piecesInARow = 0
                winCoords = []
            count += 1
                
    #If we get down here, it means that we didn't find a win in any direction,
    #so we return False to indicate the lack of a win and blank winCoords
    return (False, [])                

def findWinFullTable(table, winLength):
    
    '''Discovers if there is a win anywhere on table.'''

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
    
    '''Places a piece into inTable in column placeCol.  The type of piece is
    determined by whoseTurn.
    
    Returns a list.  curTable is the updated table.  placedPiece is a boolean
    indicating if a piece was successfully placed (a piece can fail to be
    placed if placeCol was already full.)  xCoord and yCoord are the X and Y
    coordinates of the placed piece.
    '''

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
        
    #Return the updated table, whether or not a piece was placed, and the
    #coordinates of the placed piece (if any)
    if placedPiece:
        xCoord = placeCol
        yCoord = count
    else:
        xCoord = -1
        yCoord = -1
        
    return[curTable, placedPiece, xCoord, yCoord]
    
def chooseCard(table, playerCards, opponentCards, winLength, lastCol,
               whoseTurn, helpHurt, mostLeastAverage="average"):
    
    '''Chooses a card to play based upon the inputs.  table is the input table.
    playerCards are the current cards of the player who's deciding which card
    to play.  opponentCards are the opponent's cards.  winLength is the length
    in a row required to win the game.  lastCol is the previous column in which
    a piece was (attempted to be) placed.  whoseTurn is 1 for the red player
    and 2 for the black player and indicates what color piece is next to be
    placed.
    
    helpHurt is "help" if the current player is trying to make a
    placement helpful to whosever turn it is, "hurt" if the current player is
    trying to make a placement hurtful to whosever turn it is, and "random" if
    the card choice is to be random.  mostLeastAverage is "most" if the current
    player is aiming for the most helpful or hurtful outcome, "least" if the
    current player is aiming for the least helpful or hurtful outcome, or
    "average" if the current player is making its help or hurt decision based
    upon the average outcome for each card it could choose.
    '''
    
    print(helpHurt + " " + str(mostLeastAverage))
    
    #If we're doing a random draw, just pick the card here and skip the
    #silliness below
    if helpHurt == "random":
        return (random.sample(playerCards, 1))
    
    #Get the set of all possible combinations that could be made in the
    #next turn
    allSums = {}

    for x in opponentCards:
        for y in playerCards:
            allSums[x+y] = 0
    
    #For each entry in allSums, classify it as -2 if it causes a win or -1 if
    #it prevents an opponent's win.  Otherwise, score it according to the
    #algorithm in calcPlacementValue, scoring both for offensive and
    #defensive value.
    
    #List to hold all of the classifications that the current sum could be
    #given
    for num in allSums:
    
        #Now test each number in allSums to see if it causes a win.  If not,
        #calculate the value of that placement.
        testTable, placedPiece, xPlace, yPlace = placePiece(table,
                                                            (lastCol+num) % len(table[0]),
                                                            whoseTurn)
        
        #If we couldn't place the piece, score the sum a 0
        if not placedPiece:
            allSums[num] = 0
            continue
        
        #If the piece was placed, first see if we have a win.  If so, score the
        #sum a -2.  If we don't, get the placement's value from
        #calcPlacementValue and call that the offensive value of the placement.
        foundTestWin, _ = findWinCurPiece(testTable, xPlace, yPlace, winLength)
        if foundTestWin:
            allSums[num] = -2
        else:
            offenseValue = calcPlacementValue(testTable, xPlace, yPlace,
                                              winLength)
        
        #Now do the analysis again but place an opposing piece in the space
        #unless we've already scored the piece (0 because the column is full or
        #-2 because it causes a win)
        if whoseTurn == 1: oppoTurn = 2
        else: oppoTurn = 1
        testTable, placedPiece, xPlace, yPlace = placePiece(table,
                                                            (lastCol+num) % len(table[0]),
                                                            oppoTurn)
        
        #First see if we have a win.  If so, score the sum a -1.  If we don't,
        #get the placement's value from calcPlacementValue and call that the
        #defensive value of the placement.
        foundTestWin, _ = findWinCurPiece(testTable, xPlace, yPlace, winLength)
        if foundTestWin:
            allSums[num] = -1
        else:
            defenseValue = calcPlacementValue(testTable, xPlace, yPlace,
                                              winLength)   
            
        #Now add offenseValue and defenseValue together to get the value of
        #the piece placement, unless we already found a win for either player.        
        if allSums[num] == 0 and placedPiece:
            pieceValue = offenseValue + defenseValue
            
            #Now calculate the value of a piece placed directly above the
            #current piece.  If that piece leads to a player win, multiply the
            #current piece's score by 1.5.  If that piece leads to an opponent
            #win, divide the current piece's score by 1.5.  Otherwise,
            #subtract the score for the opponent's piece from the score for the
            #current player's piece, then multiply that by 0.5 and add it to
            #the score for the current piece.
            testTable2, placedPiece, xPlace, yPlace = placePiece(testTable,
                                                                 (lastCol+num) % len(table[0]),
                                                                 whoseTurn)
            
            #Don't bother with the remaining calculations if we've reached the
            #top of the board
            if placedPiece:
            
                foundTestWin, _ = findWinCurPiece(testTable2, xPlace, yPlace,
                                               winLength)
                if foundTestWin:
                    allSums[num] *= 1.5
                else:
                    offenseValue2 = calcPlacementValue(testTable2, xPlace,
                                                       yPlace, winLength)
                    
                testTable2, placedPiece, xPlace, yPlace = placePiece(testTable,
                                                                     (lastCol+num) % len(table[0]),
                                                                     oppoTurn)
                foundTestWin, _ = findWinCurPiece(testTable2, xPlace, yPlace,
                                               winLength)
                
                if foundTestWin:
                    allSums[num] /= 1.5
                else:
                    defenseValue2 = calcPlacementValue(testTable2, xPlace,
                                                       yPlace, winLength)
                    
                #Now try to use the offenseValue2 and defenseValue2 variables.  If
                #they exist, then foundTestWin was false in both of the previous
                #piece tests and we should use the offenseValue2 and defenseValue2
                #values.  If they don't exist, then we'll raise a NameError and
                #just keep the allSums[num] value as is.
                try:
                    allSums[num] = pieceValue + (offenseValue2 - defenseValue2) * 0.5
                except NameError:
                    pass

    print(allSums)
    
    #Now, for scoring averaging purposes, reclassify all -2s as 4 times the
    #highest score found in allSums and reclassify all -1s as 2 times the
    #highest score found in allSums.
    selfWinScore = 4 * max(allSums.values())
    oppoWinScore = 2 * max(allSums.values())
    for num in allSums:
        if allSums[num] == -2:
            allSums[num] = selfWinScore
        elif allSums[num] == -1:
            allSums[num] = oppoWinScore
            
    print(allSums)
            
    #Classify each of the playerCards.  Start by assembling all of the possible
    #placement values that are accessible by playing the given card.
    playerCardsDict = {}
    for x in playerCards:
        for y in opponentCards:
            curSum = x+y
            #If this sum hasn't been evaluated before, just give it the present
            #value.  Otherwise, give it -2 if the current value is -2, -1 if
            #the current value is -1 and that sum isn't already -2, and the
            #min or max of the sum's value and the current value, depending
            #upon the chosen strategy.
            if x not in playerCardsDict:
                playerCardsDict[x] = [allSums[curSum]]
            else:
                playerCardsDict[x].append(allSums[curSum])
    print(playerCardsDict)
    print("---")
            
    #Consolidate all of the values in playerCardsDict.  If we're helping or
    #hurting on average, then take the average of each list of values.
    #Otherwise, take the max of each list of values if we're helping and the
    #min if we're hurting.
    if mostLeastAverage == "average":
        for x in playerCardsDict:
            playerCardsDict[x] = sum(playerCardsDict[x])/len(playerCardsDict[x])
    elif helpHurt == "help":
        for x in playerCardsDict:
            playerCardsDict[x] = max(playerCardsDict[x])
    else:
        for x in playerCardsDict:
            playerCardsDict[x] = min(playerCardsDict[x])
            
    #OMG now we'll finally choose the next card!
    
    #Assemble a list of cards that are the top candidates for selection
    candidateCardsList = []
        
    #If we're helping the most, helping on average, or hurting the least,
    #get the highest score from playerCardsDict. Otherwise, if we're hurting
    #the most, hurting on average, or helping the least, get the lowest score.
    if (helpHurt, mostLeastAverage) in [("help","most"),("help","average"),
       ("hurt","least")]:
        bestScore = playerCardsDict[max(playerCardsDict,
                                       key=playerCardsDict.get)]
    else:
        bestScore = playerCardsDict[min(playerCardsDict,
                                       key=playerCardsDict.get)]
    print ("Best score: " + str(bestScore))
    
    #Now add cards to candidateCardsList that match bestScore
    for card, value in playerCardsDict.items():
        if value == bestScore:
            candidateCardsList.append(card)
    
    #Now choose any card in candidateCardsList
    return (random.sample(candidateCardsList,1)[0])

def calcCircleCoords(ulBoxX, ulBoxY, boxSideLength, diameterLengthFactor):
    
    '''Calculates the canvas coordinates for a circle based upon the upper
    left coordinates of the table square in which the circle should go.
    
    ulBoxX and ulBoxY are the X and Y canvas coordinates of the table square
    in which the circle should go.  boxSideLength is the length in pixels of
    the side of the box.  diameterLengthFactor is a real number indicating the
    intended ratio of the diameter of the circle to the length of the square
    side.  A value of 1 means that the circle should fill the box.  Less than
    1 means that the circle's diameter should be shorter than the box side.
    '''
    
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
        
        '''Initialize the table, the player cards, the previous column, the
        turn count, and whose turn it is.
        '''
    
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
        
        '''Wrap eveything up if the game is over.  Announce the winner or if
        there is no winner, outline the winning pieces if any, and disable
        further card inputs.
        '''
        
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

    def checkTable(self, xCoord, yCoord):
        
        #If xCoord and yCoord are both -1, it means that a piece couldn't be
        #placed, so don't try to look for a win in that case
        
        if [xCoord, yCoord] != [-1,-1]:
            #Get a win if any
            self.foundWin, self.winCoords = findWinCurPiece(self.table, xCoord,
                                                            yCoord, self.nwin)
        
#        #Check the status of the current game board
#        self.gameOver, self.foundWin, self.winCoords = findWinFullTable(self.table,
#                                                               self.nwin)
                
        #End the game if the board is full
        if self.foundWin or not any(" " in row for row in self.table):
            self.gameOver = True
        else:
            self.gameOver = False
        
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
                    chooseType = "help"
                else:
                    chooseType = "hurt"
                onAverage = True
                p1Card = chooseCard(self.table, self.p1Cards, self.p2Cards,
                                    self.nwin, self.lastCol, self.whoseTurn,
                                    chooseType, onAverage)
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
                helpHurt = "hurt"
            else:
                helpHurt = "help"
            mostLeastAverage = "average"
            p2Card = chooseCard(self.table, self.p2Cards, self.p1Cards,
                                self.nwin, self.lastCol, self.whoseTurn,
                                helpHurt, mostLeastAverage)
        
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
        self.table, placedPiece, pieceXCoord, pieceYCoord = placePiece(self.table,
                                                                       self.lastCol,
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
        self.checkTable(pieceXCoord, pieceYCoord)
    
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
        self.drawGameBool.set(1)
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
        self.nWinEntry.insert(0,"4")
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