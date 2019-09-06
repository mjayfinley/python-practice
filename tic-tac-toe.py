board = [['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]']]


for row in board:
    print(row)

player = input('Are you player X or Y? ')
row = int(input('Enter row 0-2 you would like to play on: '))
column = int(input('Enter columen 0-2 you would like to play on: '))
location = (row, column)


def move(board, location, player):
    for i in range(len(board)):
        for j in range(len(board)):
            if location == (i, j):
                board[i][j] = player
    for row in board:
        print(row)


move(board, location, player)


# while win condition not met - loop

# win conditions

# alternate players
