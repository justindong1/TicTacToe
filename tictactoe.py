# Tic Tac Toe
# Made by Justin Dong 1/20/2018
import random

def drawBoard(board):
# Draws a board of 9 spaces using | and a list of 10 strings.
# The item at index 0 is ignored for better comprehension of the numbering on the board.
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def setPlayersLetter():
# Player chooses what letter they want to play as between X or O.
##    playersLetter = ""
    print("What letter do you want?")
    playersLetter = input().upper()
    computersLetter = ""
    if (playersLetter != "X" and playersLetter != "O"):
        print("You can only choose X or O")
        print("Choose X or O")
        playersLetter = input().upper()
    if (playersLetter == "O"):
        return ['O','X']
    else:
        return ['X', 'O']

def whoStarts():
    x = random.randint(0,1)
    if (x == 0):
        return 'Player'
    else:
        return 'Computer'

def playAgain():
    x = ''
    print("Do you want to play again?")
    x = input()
    if x.lower().startswith('y'):
        return True
    else:
        return False

def makeMove(board,letter,move):
    board[move] = letter

def getPlayerMove(board):
    move = ""
    while move not in '1 2 3 4 5 6 7 8 9'.split():
        print("What is your move?")
        move = input()
    return int(move)

def getBoardCopy(board):
    copy = []
    for i in board:
        copy.append(i)
    return copy

def chooseRandomMove(board,movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def isSpaceFree(board,num):
    if board[num] != ' ':
        return False
    else:
        return True

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True

def isWinner(board,le):
    #Return whether anyone won based on board and letter
    return ((board[7] == le and board[8] == le and board[9] == le) or #across the top
    (board[4] == le and board[5] == le and board[6] == le) or #across the middle
    (board[1] == le and board[2] == le and board[3] == le) or #across the bottom
    (board[1] == le and board[4] == le and board[7] == le) or #left side
    (board[2] == le and board[5] == le and board[8] == le) or #middle
    (board[3] == le and board[6] == le and board[9] == le) or #right side
    (board[7] == le and board[5] == le and board[3] == le) or #diagonal 653
    (board[1] == le and board[5] == le and board[9] == le)) #diagonal 159
            

def getComputerMove(board,computersLetter):
    randomNum = random.randint(0,10)
    if computersLetter == 'X':
        playersLetter == 'O'
    else:
        playersLetter == 'X'
        
    #Check to see if we can win 
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,computersLetter, i)
            if isWinner(copy,computersLetter):
                return i
            
    #Check if player could win
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy,playersLetter,i)
            if isWinner(copy,playersLetter):
                if randomNum < 7:
                    return i 

    #Try to take a corner
    move = chooseRandomMove(board,[1,3,7,9])
    if move != None:
        return move
            
    #Try to take center
    if isSpaceFree(board,5):
        return 5
    
    #Take any move
    return chooseRandomMove(board,[2,4,6,8])
      
        
while True:
    #Reset the board
    theBoard = [' '] * 10
    playersLetter, computersLetter = setPlayersLetter()
    turn = whoStarts()
    print(turn + " will start!")
    gameInProgress = True

    while (gameInProgress == True):
        if turn == 'Player':
            #Player's move
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playersLetter,move)

            if (isWinner(theBoard,playersLetter)):
                drawBoard(theBoard)
                print("You have matched three in a row.")
                print("You win!")
                gameInProgress = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("It's a tie!")
                    break
                else:
                    turn = 'Computer'
        else:
            #Computer's move
            move = getComputerMove(theBoard,computersLetter)
            makeMove(theBoard,computersLetter,move)

            if isWinner(theBoard,computersLetter):
                drawBoard(theBoard)
                print("The computer has won!")
                gameInProgress = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("It's a tie!")
                    break
                else:
                    turn = 'Player'

    if playAgain():
        gameInProgress = True
    else:
        break
                
    



    
    


    
    

