# Tic Tac Toe
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
    playersLetter = ""
    print("What letter do you want?")
    playersLetter = input().upper()
    computersLetter = ""
    if (playersLetter != "X" and playersLetter != "O"):
        print("You can only choose X or O")
        print("Choose X or O")
        playersLetter = input().upper()
    if (playersLetter == "O"):
        computersLetter == "X"
    else:
        computersLetter == "O"
    return [playersLetter,computersLetter]

def whoStarts():
    x = random.randint(0,1)
    if (x == 0):
        return 'player'
    else:
        return 'computer'

def makeMove(board):
    drawBoard(board)

while True:
    #Reset the board
    board = [' '] * 10
    playersLetter, computersLetter = setPlayersLetter()
    turn = whoStarts()
    print(turn + " will start!")
    gameIsPlaying = True
    



    
    


    
    

