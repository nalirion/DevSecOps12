# printing the board
def printboard(args):
    for i in range(3):
        print(args[i])

# check who is the winner
def checkwinner(args):
    if args == [['x', '_', '_'], ['x', '_', '_'], ['x', '_', '_']]:
        return 1
    elif args == [['_', 'x', '_'], ['_', 'x', '_'], ['_', 'x', '_']]:
        return 1
    elif args == [['_', '_', 'x'], ['_', '_', 'x'], ['_', '_', 'x']]:
        return 1
    elif args == [['x', 'x', 'x'], ['_', '_', '_'], ['_', '_', '_']]:
        return 1
    elif args == [['_', '_', '_'], ['x', 'x', 'x'], ['_', '_', '_']]:
        return 1
    elif args == [['_', '_', '_'], ['_', '_', '_'], ['x', 'x', 'x']]:
        return 1
    elif args == [['x', '_', '_'], ['_', 'x', '_'], ['_', '_', 'x']]:
        return 1
    elif args == [['_', '_', 'x'], ['_', 'x', '_'], ['x', '_', '_']]:
        return 1
    elif args == [['o', '_', '_'], ['o', '_', '_'], ['o', '_', '_']]:
        return 2
    elif args == [['_', 'o', '_'], ['_', 'o', '_'], ['_', 'o', '_']]:
        return 2
    elif args == [['_', '_', 'o'], ['_', '_', 'o'], ['_', '_', 'o']]:
        return 2
    elif args == [['o', 'o', 'o'], ['_', '_', '_'], ['_', '_', '_']]:
        return 2
    elif args == [['_', '_', '_'], ['o', 'o', 'o'], ['_', '_', '_']]:
        return 2
    elif args == [['_', '_', '_'], ['_', '_', '_'], ['o', 'o', 'o']]:
        return 2
    elif args == [['o', '_', '_'], ['_', 'o', '_'], ['_', '_', 'o']]:
        return 2
    elif args == [['_', '_', 'o'], ['_', 'o', '_'], ['o', '_', '_']]:
        return 2


while True:  # for running the program
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    draw = 0
    print("welcome to the game")
    print("please enter row and line")
    while True:  # starting the game
        while True:  # while there is a place to insert the input and checks if its legal input for player o
            try:
                row = int(input('player x please insert number between 0-2 for row: '))
            except ValueError:
                continue
            try:
                line = int(input('player x please insert number between 0-2 for line: '))
            except ValueError:
                continue

            # check that the input is correct then insert the turn of x
            if -1 < row < 3:
                if -1 < line < 3:
                    if board[row][line] == '_':
                        board[row][line] = 'x'
                        draw += 1  # counting the number of free space on the board
                        break
                    elif board[row][line] == 'o' or board[row][line] == 'x':
                        print('this place already taken please choose other one')
            else:
                print('wrong input')
        printboard(board)
        if checkwinner(board) == 1:  # check if the winner is x
            print("player x wins!")
            break
        elif draw == 9:
            print("it's a draw!")
            break
        while True:  # while there is a place to insert the input and checks if its legal input for payer o
            try:
                row = int(input('player o please insert number between 0-2 for row: '))
            except ValueError:
                continue
            try:
                line = int(input('player o please insert number between 0-2 for line: '))
            except ValueError:
                continue

            # check that the input is correct then insert the turn of o
            if -1 < row < 3:
                if -1 < line < 3:
                    if board[row][line] == '_':
                        board[row][line] = 'o'
                        draw += 1  # counting the number of free space on the board
                        break
                    elif board[row][line] == 'o' or board[row][line] == 'x':
                        print('this place already taken please choose other one')
            else:
                print('wrong input')
            # print the board after every input of the turn of the player
        printboard(board)
        if checkwinner(board) == 2:
            print("player o wins!")
            break  # stops the game
        elif draw == 9:  # counting the number of free space on the board
            print("it's a draw!")
            break  # stops the game

    answer = input(print("do you want another game? y/n "))
    if answer == 'n':
        break
