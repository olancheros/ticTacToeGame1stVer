'''
    Tic Tac Toe Game

    Tic Tac Toe is a game played between two players played on a 3 x 3 square grid.
    Each player inhabits a cell in their respective turns, keeping the objective of placing
    three similar signs (X or O) in a vertical, horizontal, or diagonal pattern.
    In this case a player has to play against the computer.

'''

import random

def displayBoard(board):
    '''
    This function prints the board on its initial empty state
    '''

    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[1] + '   |   ' + board[2] + '   |   ' + board[3] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[4] + '   |   ' + board[5] + '   |   ' + board[6] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[7] + '   |   ' + board[8] + '   |   ' + board[9] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')


'''-------------------------------------------------------------------------------------'''

def selectSign():
    '''
    This function allows the player to select the sign to play with
    '''

    sign = ''
    while not(sign == 'X' or sign == 'O'):
        print('\nPlease select X or O to start the game\n')
        sign = input().upper()

    if sign == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

'''-------------------------------------------------------------------------------------'''

def selectFstPlayer():
    '''
    The random function selects who will play first.
    '''

    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'


'''-------------------------------------------------------------------------------------'''

def playAgain():
    '''
    This function is to select if the player wants to continue or not
    '''
    tryAgain =''
    while not(tryAgain == 'y' or tryAgain == 'n'):
        tryAgain = input('\nDo you want to continue? (y or n)\n')
        if tryAgain.lower() == 'y':
            return True
        elif tryAgain.lower() == 'n':
            return False
        else:
            print('Please hit a valid key\n')


'''-------------------------------------------------------------------------------------'''

def enterMove(board, sign, move):
    '''
    Add the sign into the selected place
    '''
    board[move] = sign


'''-------------------------------------------------------------------------------------'''

def victoryFor(board, sign):
    '''
    Depending of the board and sign, the function returns TRUE if that player has won
    '''
    return ((board[1] == sign and board[2] == sign and board[3] == sign) or # Top row
            (board[4] == sign and board[5] == sign and board[6] == sign) or     # Mid row
            (board[7] == sign and board[8] == sign and board[9] == sign) or     # bottom row
            (board[1] == sign and board[4] == sign and board[7] == sign) or     # left col
            (board[2] == sign and board[5] == sign and board[8] == sign) or     # Mid col
            (board[3] == sign and board[6] == sign and board[9] == sign) or     # Right col
            (board[1] == sign and board[5] == sign and board[9] == sign) or     # Diagonal
            (board[3] == sign and board[5] == sign and board[7] == sign))        # Diagonal



'''-------------------------------------------------------------------------------------'''

def updateBoard(board):
    '''
    Function to make a copy of the board list and update it with the last move
    '''
    copyBoard = []
    for i in board:
        copyBoard.append(i)
    return copyBoard

'''-------------------------------------------------------------------------------------'''

def isFieldFree(board, move):
    '''
    Checks if the position is empty
    '''
    return board[move] == ' '


'''-------------------------------------------------------------------------------------'''

def playerMove(board):
    '''
    This function asks for the next move and checks if the entry is valid or not
    '''
    move = '  '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not  isFieldFree(board, int(move)):
        print('\nWhat is your next move? (1-9)\n')
        move = input()
    return int(move)


'''-------------------------------------------------------------------------------------'''

def randomMoveFromList(board, moveList):
    possibleMoves =[]
    for i in moveList:
        if isFieldFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


'''-------------------------------------------------------------------------------------'''


def computerMove(board, computerSign):
    '''
    Given a board and computer's sign, determine where to move and return that move
    '''

    if computerSign == 'X':
        playerSign = 'O'
    else:
        playerSign = 'X'

    for i in range(1, 10):
        copy = updateBoard(board)
        if isFieldFree(copy, i):
            enterMove(copy, playerSign, i)
            if victoryFor(copy, playerSign):
                return i

    for i in range(1, 10):
        copy = updateBoard(board)
        if isFieldFree(copy, i):
            enterMove(copy, playerSign, i)
            if victoryFor(copy, playerSign):
                return i

    move = randomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isFieldFree(board, 5):
        return 5

    return randomMoveFromList(board, [2, 4, 6, 8])


'''-------------------------------------------------------------------------------------'''


def isBoardFull(board):
    for i in range(1, 10):
        if isFieldFree(board, i):
            return False
    return True


'''-------------------------------------------------------------------------------------'''


'''
    Outer Game Loop
'''

print('\n\n**********Welcome to Tic Tac Toe**********\n')
print(' The following image shows the number key')
print('       distribution to play with\n\n')

print('        +-------+-------+-------+')
print('        |       |       |       |')
print('        |   ' + '1' + '   |   ' + '2' + '   |   ' + '3' + '   |')
print('        |       |       |       |')
print('        +-------+-------+-------+')
print('        |       |       |       |')
print('        |   ' + '4' + '   |   ' + '5' + '   |   ' + '6' + '   |')
print('        |       |       |       |')
print('        +-------+-------+-------+')
print('        |       |       |       |')
print('        |   ' + '7' + '   |   ' + '8' + '   |   ' + '9' + '   |')
print('        |       |       |       |')
print('        +-------+-------+-------+')

print('\n\n**********Are you ready to play?**********\n')

while True:
    '''Clean the board'''
    theBoard = [' '] * 10
    playerSign, computerSign = selectSign()
    turn = selectFstPlayer()
    print('\nThe ' + turn + ' will go first\n')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            '''Player's turn'''
            displayBoard(theBoard)
            move = playerMove(theBoard)
            enterMove(theBoard, playerSign, move)

            if victoryFor(theBoard, playerSign):
                displayBoard(theBoard)
                print('\nYou have won the game!\n')
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    displayBoard(theBoard)
                    print('\nThe game is tie\n')
                    break
                else:
                    turn = 'computer'

        else:
            '''Computer's turn'''
            move = computerMove(theBoard, computerSign)
            enterMove(theBoard, computerSign, move)

            if victoryFor(theBoard, computerSign):
                displayBoard(theBoard)
                print('\nThe computer has beaten you!\n')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    displayBoard(theBoard)
                    print('\nThe game is tie\n')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
