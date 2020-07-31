# ---- Global Vars ---- #

gameStillGo = True

board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

winner = None

currentPlayer = "X"
# board
# UI
# Game Rules
# Check Turn
# Win Condition
    # check row
    # check columns 
    # check diagonals 
# Tie Condition
# Switch User turn

def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def playGame():

    displayBoard()

    while gameStillGo:

        handleTurn(currentPlayer)
        checkIfGameOver()
        flipPlayer()
        playAgain()
        
    # End of Game
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


def handleTurn(player):
    print(player + "'s turn.")
    postion = input("Choose a position from 1-9: ")

    valid = False

    #check for validation and put x or o on board
    while not valid:

        while postion not in ["1","2","3","4","5","6","7","8","9"]:
            postion = input("Choose a position from 1-9: ")


        postion = int(postion) - 1

        if board[postion] == "-":
            valid = True
        else:
            print("Invalid spot: Pick again.")


    board[postion] = player
    displayBoard()

def checkIfGameOver():
    checkForWinner()
    checkForTie()

def checkForWinner():

    global winner

    #check rows
    rowWinner = checkRows()
    #check colums
    columnsWinner = checkColumns()
    #check diagonals 
    diagonalsWinner = checkDiagonals()

    if rowWinner:
        winner = rowWinner
    elif columnsWinner:
        winner = columnsWinner
    elif diagonalsWinner:
        winner = diagonalsWinner
    else:
        winner = None
    return

def checkRows():
    global gameStillGo

    #check rows values are equal
    rowOne = board[0] == board[1] == board[2] != "-"
    rowTwo = board[3] == board[4] == board[5] != "-"
    rowThree = board[6] == board[7] == board[8] != "-"

    if rowOne or rowTwo or rowThree:
        gameStillGo = False
    if rowOne:
        return board[0]  
    elif rowTwo:
        return board[3]
    elif rowThree:  
        return board[6] 
    return

def checkColumns():
    global gameStillGo

    #check columns values are equal
    columnsOne = board[0] == board[3] == board[6] != "-"
    columnsTwo = board[1] == board[4] == board[7] != "-"
    columnsThree = board[2] == board[5] == board[8] != "-"

    if  columnsOne or  columnsTwo or  columnsThree:
        gameStillGo = False
    if  columnsOne:
        return board[0]  
    elif columnsTwo:
        return board[1]
    elif columnsThree:  
        return board[2] 
    return

def checkDiagonals():
    global gameStillGo

    #check columns values are equal
    diagonalsOne = board[0] == board[4] == board[8] != "-"
    diagonalsTwo = board[6] == board[4] == board[2] != "-"

    if  diagonalsOne or  diagonalsTwo:
        gameStillGo = False
    if  diagonalsOne:
        return board[0]  
    elif diagonalsTwo:
        return board[6]
    return


def checkForTie():
    global gameStillGo
    if "-" not in board:
        gameStillGo = False
    return

def flipPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"
    return

def playAgain():
    if gameStillGo == False:
        newGame()
    return

def newGame():
    print("Would you like to play again ")
    return


playGame() 