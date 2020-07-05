# This is a tic-tac-toe game for 2 players. Use the number pad to specify the position of X / O.

print("\n\t\t\t\t\t\tTIC-TAC-TOE\n")

def printBoard(board):
    print('     |     |     ')
    print('  ' + board['7'] + '  |  ' + board['8'] + '  |  ' + board['9'])
    print('     |     |     ')
    print('-----+-----+-----')
    print('     |     |     ')
    print('  ' + board['4'] + '  |  ' + board['5'] + '  |  ' + board['6'])
    print('     |     |     ')
    print('-----+-----+-----')
    print('     |     |     ')
    print('  ' + board['1'] + '  |  ' + board['2'] + '  |  ' + board['3'])
    print('     |     |     ')

# Take the first player's input
def player1(board):
    while ' ' in board.values():
        x = input('Player-1 >> Enter the position where you want to enter "X": ')
        try:
            if int(x):
                if 0<int(x) and int(x)<10:
                    if board[x] == ' ':
                        board[x] = 'X'
                        return board
                    else:
                        print("This position is already occupied, Specify some other position")
                        continue
                else:
                    print("Enter a number between 1-9.")
                    continue
        except Exception:
            print("Please enter a number.")
            continue

# Take the second player's input
def player2(board):
    while ' ' in board.values():
        x = input('Player-2 >> Enter the position where you want to enter "O": ')
        try:
            if int(x):
                if 0<int(x) and int(x)<10:
                    if board[x] == ' ':
                        board[x] = 'O'
                        return board
                    else:
                        print("This position is already occupied, Specify some other position")
                        continue
                else:
                    print("Enter a number between 1-9.")
                    continue
        except Exception:
            print("Please enter a number.")
            continue

def checkWinner(board, letter):
    if((board['1'] == letter and board['2'] == letter and board['3'] == letter) or
       (board['4'] == letter and board['5'] == letter and board['6'] == letter) or
       (board['7'] == letter and board['8'] == letter and board['9'] == letter) or
       (board['7'] == letter and board['4'] == letter and board['1'] == letter) or
       (board['8'] == letter and board['5'] == letter and board['2'] == letter) or
       (board['9'] == letter and board['6'] == letter and board['3'] == letter) or
       (board['1'] == letter and board['5'] == letter and board['9'] == letter) or
       (board['7'] == letter and board['5'] == letter and board['3'] == letter)) :
        if letter == 'X':
            print("\n-----------X wins!------------\n")
            exit()
        elif letter == 'O':
            print("\n-----------O wins!------------\n")
            exit()
    elif ' ' not in board.values():
        print("\n-------------It's a tie!-------------\n")
        exit()
            
board = {'7': ' ', '8': ' ','9': ' ',
         '4': ' ', '5': ' ','6': ' ',
         '1': ' ', '2': ' ','3': ' '}
while ' ' in board.values():
    if ' ' in board.values():
        player1(board)
        printBoard(board)
        for letter in ['X','O']:
            checkWinner(board,letter)
    if ' ' in board.values():
        player2(board)
        printBoard(board)
        for letter in ['X','O']:
            checkWinner(board,letter)