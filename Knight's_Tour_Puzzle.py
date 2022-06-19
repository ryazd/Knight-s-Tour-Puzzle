import copy


def put_knight(board, x, y, c):
    if board[y - 1][x - 1] == '__' or '_X':
        board[y - 1][x - 1] = " " + c
    else:
        board[y - 1][x - 1] = "  " + c


def print_board(board, x, y):
    i = y - 1
    cell_size = 2 if x < 10 else 3
    num_of = x * (cell_size + 1) + 3
    print(' ' + '-' * num_of)
    while i >= 0:
        s = str(i + 1) + '| '
        if y >= 10 and i < 10:
            s = ' ' + s
        for j in range(x):
            s += str(board[i][j]) + ' '
        s += '|'
        print(s)
        i -= 1
    print(' ' + '-' * num_of)
    s = ' ' * cell_size * 2
    for i in range(x):
        s += str(i + 1) + ' ' * cell_size
    print(s)


def print_solve_board(board, x, y):
    i = y - 1
    cell_size = len(str(x * y))
    num_of = x * (cell_size + 1) + 3
    print(' ' + '-' * num_of)
    while i >= 0:
        s = str(i + 1) + '| '
        for j in range(x):
            s += ' ' * (cell_size - len(str(board[i][j]))) + str(board[i][j]) + ' '
        s += '|'
        print(s)
        i -= 1
    print(' ' + '-' * num_of)
    s = ' ' * cell_size * 2
    for i in range(x):
        s += str(i + 1) + ' ' * cell_size
    print(s)


def check_position(x_b, y_b):
    while True:
        pos = input("Enter the knight's starting position: ").split()
        if not len(pos) == 2:
            print("Invalid dimensions!")
        else:
            try:
                x = int(pos[0])
                y = int(pos[1])
                if 1 <= x <= x_b and 1 <= y <= y_b:
                    return x, y
                else:
                    print("Invalid dimensions!")
            except ValueError:
                print("Invalid dimensions!")


def check_board_size():
    while True:
        board_size = input("Enter your board dimensions: ").split()
        if not len(board_size) == 2:
            print("Invalid dimensions!")
        else:
            try:
                x = int(board_size[0])
                y = int(board_size[1])
                if x > 0 and y > 0:
                    return x, y
                else:
                    print("Invalid dimensions!")
            except ValueError:
                print("Invalid dimensions!")


def init_board():
    x, y = check_board_size()
    board = []
    c = '__'
    if x > 9:
        c += '_'
    for i in range(y):
        board.append([c] * x)
    return board, x, y, c


def possible_moves(board, x_k, y_k, x_b, y_b, first):
    num_of_moves = 0
    if x_k + 2 <= x_b and y_k + 1 <= y_b and not '*' in str(board[y_k][x_k + 1]):
        if first == 1:
            num_of_moves += 1
        else:
            num_of_moves = possible_moves(board, x_k + 2, y_k + 1, x_b, y_b, 1)
            put_knight(board, x_k + 2, y_k + 1, str(num_of_moves - 1))
    if x_k + 1 <= x_b and y_k + 2 <= y_b and not '*' in str(board[y_k + 1][x_k]):
        if first == 1:
            num_of_moves += 1
        else:
            num_of_moves = possible_moves(board, x_k + 1, y_k + 2, x_b, y_b, 1)
            put_knight(board, x_k + 1, y_k + 2, str(num_of_moves - 1))
    if x_k + 2 <= x_b and y_k - 1 >= 1 and not '*' in str(board[y_k - 2][x_k + 1]):
        if first == 1:
            num_of_moves += 1
        else:
            num_of_moves = possible_moves(board, x_k + 2, y_k - 1, x_b, y_b, 1)
            put_knight(board, x_k + 2, y_k - 1, str(num_of_moves - 1))
    if x_k + 1 <= x_b and y_k - 2 >= 1 and not '*' in str(board[y_k - 3][x_k]):
        if first == 1:
            num_of_moves += 1
        else:
            num_of_moves = possible_moves(board, x_k + 1, y_k - 2, x_b, y_b, 1)
            put_knight(board, x_k + 1, y_k - 2, str(num_of_moves - 1))
    if x_k - 1 >= 1 and y_k + 2 <= y_b and not '*' in str(board[y_k + 1][x_k - 2]):
        if first == 1:
            num_of_moves += 1
        else:
            num_of_moves = possible_moves(board, x_k - 1, y_k + 2, x_b, y_b, 1)
            put_knight(board, x_k - 1, y_k + 2, str(num_of_moves - 1))
    if x_k - 2 >= 1 and y_k + 1 <= y_b and not '*' in str(board[y_k][x_k - 3]):
        if first == 1:
            num_of_moves += 1
        else:
            num_of_moves = possible_moves(board, x_k - 2, y_k + 1, x_b, y_b, 1)
            put_knight(board, x_k - 2, y_k + 1, str(num_of_moves - 1))
    if x_k - 1 >= 1 and y_k - 2 >= 1 and not '*' in str(board[y_k - 3][x_k - 2]):
        if first == 1:
            num_of_moves += 1
        else:
            num_of_moves = possible_moves(board, x_k - 1, y_k - 2, x_b, y_b, 1)
            put_knight(board, x_k - 1, y_k - 2, str(num_of_moves - 1))
    if x_k - 2 >= 1 and y_k - 1 >= 1 and not '*' in str(board[y_k - 2][x_k - 3]):
        if first == 1:
            num_of_moves += 1
        else:
            num_of_moves = possible_moves(board, x_k - 2, y_k - 1, x_b, y_b, 1)
            put_knight(board, x_k - 2, y_k - 1, str(num_of_moves - 1))
    return num_of_moves


def check_possible_move(board, x_k, y_k, x_b, y_b):
    num_of_moves = 0
    if x_k + 2 <= x_b and y_k + 1 <= y_b and not '*' in str(board[y_k][x_k + 1]):
        num_of_moves += 1
    if x_k + 1 <= x_b and y_k + 2 <= y_b and not '*' in str(board[y_k + 1][x_k]):
        num_of_moves += 1
    if x_k + 2 <= x_b and y_k - 1 >= 1 and not '*' in str(board[y_k - 2][x_k + 1]):
        num_of_moves += 1
    if x_k + 1 <= x_b and y_k - 2 >= 1 and not '*' in str(board[y_k - 3][x_k]):
        num_of_moves += 1
    if x_k - 1 >= 1 and y_k + 2 <= y_b and not '*' in str(board[y_k + 1][x_k - 2]):
        num_of_moves += 1
    if x_k - 2 >= 1 and y_k + 1 <= y_b and not '*' in str(board[y_k][x_k - 3]):
        num_of_moves+= 1
    if x_k - 1 >= 1 and y_k - 2 >= 1 and not '*' in str(board[y_k - 3][x_k - 2]):
        num_of_moves += 1
    if x_k - 2 >= 1 and y_k - 1 >= 1 and not '*' in str(board[y_k - 2][x_k - 3]):
        num_of_moves += 1
    return num_of_moves


def check_occupied(board, x, y):
    if board[y - 1][x - 1] == '  *' or board[y - 1][x - 1] == ' *' or board[y - 1][x - 1] == ' X' or board[y - 1][x - 1] == '  X':
        return False
    return True


def is_l_move(x_k, y_k, x, y):
    x_c = abs(x_k - x)
    y_c = abs(y_k - y)
    if x_c == 2 and y_c == 1:
        return True
    elif x_c == 1 and y_c == 2:
        return True
    return False


def check_move(board, x_b, y_b, x_k, y_k):
    pos = input("Enter your next move: ").split()
    while True:
        if not len(pos) == 2:
            print("Invalid dimensions!")
        else:
            try:
                x = int(pos[0])
                y = int(pos[1])
                if 1 <= x <= x_b and 1 <= y <= y_b and check_occupied(board, x, y) and is_l_move(x_k, y_k, x, y):
                    return x, y
                else:
                    pos = input("Invalid move! Enter your next move: ")
            except ValueError:
                pos = input("Invalid move! Enter your next move: ")


def check_end(board, c, x_k, y_k, x_b, y_b):
    num_of_free = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == c:
                num_of_free += 1
    if num_of_free == 0:
        print("What a great tour! Congratulations!")
        return True
    elif check_possible_move(board, x_k, y_k, x_b, y_b) == 0:
        print('No more possible moves!')
        num_of_visited = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if '*' in str(board[i][j]):
                    num_of_visited += 1
        print(f'Your knight visited {num_of_visited + 1} squares!')
        return True



def isSafe(x, y, board, n, m):
    if (x >= 0 and y >= 0 and x < m and y < n and board[y][x] == -1):
        return True
    return False


def solveKT(n_board, m_board, start_x, start_y, act):
    # Initialization of Board matrix
    board = [[-1 for i in range(m_board)] for i in range(n_board)]

    # move_x and move_y define next move of Knight.
    # move_x is for next value of x coordinate
    # move_y is for next value of y coordinate
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Since the Knight is initially at the first block
    board[start_y][start_x] = 1

    # Step counter for knight's position
    pos = 2

    # Checking if solution exists or not
    if (not solveKTUtil(n_board, m_board, board, start_x, start_y, move_x, move_y, pos)):
        print('No solution exists!')
        return False
    else:
        if not act:
            print("Here's the solution!")
            print_solve_board(board, m_board, n_board)
        return True



def solveKTUtil(n, m, board, curr_x, curr_y, move_x, move_y, pos):
    if pos == n * m + 1:
        return True
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if (isSafe(new_x, new_y, board, n, m)):
            board[new_y][new_x] = pos
            if (solveKTUtil(n, m, board, new_x, new_y, move_x, move_y, pos + 1)):
                return True
            board[new_y][new_x] = -1
    return False



def check_action():
    char_a = input("Do you want to try the puzzle? (y/n): ")
    if char_a == 'y':
        return True
    elif char_a == 'n':
        return False
    else:
        print('Invalid input!')
        return check_action()


def play(x_knight, y_knight, x_board, y_board, char, chess_board):
    end = True
    while end:
        put_knight(chess_board, x_knight, y_knight, 'X')
        chess_possible = copy.deepcopy(chess_board)
        possible_moves(chess_possible, x_knight, y_knight, x_board, y_board, 0)
        print_board(chess_possible, x_board, y_board)
        if check_end(chess_board, char, x_knight, y_knight, x_board, y_board):
            return end
        put_knight(chess_board, x_knight, y_knight, '*')
        x_knight, y_knight = check_move(chess_board, x_board, y_board, x_knight, y_knight)


chess_board, x_board, y_board, char = init_board()
x_knight, y_knight = check_position(x_board, y_board)
if not check_action():
    solveKT(x_board, y_board, x_knight - 1, y_knight - 1, False)
elif solveKT(x_board, y_board, x_knight - 1, y_knight - 1, True):
    play(x_knight, y_knight, x_board, y_board, char, chess_board)