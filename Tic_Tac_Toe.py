# global declerations

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
player1 = "x"
winner = None
game = True

# printing the game board

def gameboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print('----------')
    print(board[3] + " | " + board[4] + " | " + board[5])
    print('----------')
    print(board[6] + " | " + board[7] + " | " + board[8])

# take player input

def playerinput(board):
    inp = int(input("Enter a number 1-9:"))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = player1
    elif board[inp - 1] == "x" or board[inp - 1] == "o":
        print('Invalid Input' + '\n' + 'Enter again')
        while game:
            gameboard(board)
            playerinput(board)
            break
    else:
        print('Invalid Input' + '\n' + 'Enter another input')

# check for win or tie

def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkvertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[5]
        return True

def checkdiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[4]
        return True

def checktie(board):
    global game
    if "-" not in board:
        gameboard(board)
        print('It is a tie!')
        game = False
        exit()

def checkwin():
    global game
    if checkhorizontal(board) or checkvertical(board) or checkdiag(board):
        gameboard(board)
        print(f"The winner is {winner}")
        game = False
        exit()

# player 2

def switchplayer():
    global player1
    if player1 == "x":
        player1 = "o"
    else:
        player1 = "x"

# Game output

while game:
    gameboard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer()