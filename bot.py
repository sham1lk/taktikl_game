from copy import deepcopy

BOARD_SIZE = 4
WHITE = 'X'
BLACK = 'O'

DEPTH = 5


def bot_move(board):
    my_board = board.get_board()
    score = -999999
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if my_board[i][j] == BLACK:
                if i > 0 and my_board[i - 1][j] == ' ':
                    board_copy = deepcopy(board)
                    board_copy.make_move(i, j, i - 1, j)
                    s = minmax(False, board_copy, DEPTH)
                    if score < s:
                        score = s
                        m = (i, j, i - 1, j)

                if i < 3 and my_board[i + 1][j] == ' ':
                    board_copy = deepcopy(board)
                    board_copy.make_move(i, j, i + 1, j)
                    s = minmax(False, board_copy, DEPTH)
                    if score < s:
                        score = s
                        m = (i, j, i + 1, j)

                if j < 3 and my_board[i][j + 1] == ' ':
                    board_copy = deepcopy(board)
                    board_copy.make_move(i, j, i, j + 1)
                    s = minmax(False, board_copy, DEPTH)
                    if score < s:
                        score = s
                        m = (i, j, i, j + 1)

                if j > 0 and my_board[i][j - 1] == ' ':
                    board_copy = deepcopy(board)
                    board_copy.make_move(i, j, i, j - 1)
                    s = minmax(False, board_copy, DEPTH)
                    if score < s:
                        score = s
                        m = (i, j, i, j - 1)
    board.make_move(*m)


def minmax(maxi, board, depth):
    my_board = board.get_board()
    if board.state():
        return 10 if board.state() == BLACK else -10
    if depth == 0:
        return 0

    scores = []

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if my_board[i][j] == (BLACK if maxi else WHITE):
                if i > 0 and my_board[i - 1][j] == ' ':
                    board_copy = deepcopy(board)
                    board_copy.make_move(i, j, i - 1, j)
                    scores.append(minmax(not maxi, board_copy, depth - 1))

                if i < 3 and my_board[i + 1][j] == ' ':
                    board_copy = deepcopy(board)
                    board_copy.make_move(i, j, i + 1, j)
                    scores.append(minmax(not maxi, board_copy, depth - 1))

                if j < 3 and my_board[i][j + 1] == ' ':
                    board_copy = deepcopy(board)
                    board_copy.make_move(i, j, i, j + 1)
                    scores.append(minmax(not maxi, board_copy, depth - 1))

                if j > 0 and my_board[i][j - 1] == ' ':
                    board_copy = deepcopy(board)
                    board.make_move(i, j, i, j - 1)
                    scores.append(minmax(not maxi, board_copy, depth - 1))
    if scores:
        return max(scores) if maxi else min(scores)
    else: return -1000


def if_move(board, x, y):
    if x > 0 and board[x - 1][y] == ' ': return True
    if x < 3 and board[x + 1][y] == ' ': return True
    if y > 0 and board[x][y - 1] == ' ': return True
    if y < 3 and board[x][y + 1] == ' ': return True
    return False
