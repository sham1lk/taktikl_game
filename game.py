import os
from bot import bot_move

BOARD_SIZE = 4
WHITE = 'X'
BLACK = 'O'
LETTERS = {'A': 0, 'B': 1, 'C': 2, 'D': 3}


class Board:
    def __init__(self):
        self.board = [[' ' for i in range(BOARD_SIZE)] for k in range(
            BOARD_SIZE)]
        self.board[0] = [WHITE if i % 2 == 0 else BLACK for i in
                         range(BOARD_SIZE)]
        self.board[-1] = [WHITE if i % 2 != 0 else BLACK for i in
                          range(BOARD_SIZE)]

    def get_board(self):
        return self.board

    def make_move(self, x, y, x1, y1):
        self.board[x1][y1] = self.board[x][y]
        self.board[x][y] = ' '

    def state(self):
        for j in range(BOARD_SIZE):
            for i in range(BOARD_SIZE):
                if self.board[i][j] != ' ':
                    if 0 < i < 3:
                        if self.board[i][j] == self.board[i+1][j] and self.board[i][j] == self.board[i-1][j]:
                            return self.board[i][j]
                    if 0 < j < 3:
                        if self.board[i][j] == self.board[i][j+1] and self.board[i][j] == self.board[i][j-1]:
                            return self.board[i][j]
                    if 0 < j < 3 and 0 < i < 3:
                        if self.board[i][j] == self.board[i+1][j+1] and self.board[i][j] == self.board[i-1][j-1]:
                            return self.board[i][j]

                        if self.board[i][j] == self.board[i-1][j+1] and self.board[i][j] == self.board[i+1][j-1]:
                            return self.board[i][j]
        return False


class Game:
    def __init__(self):
        self.board = Board()
        self.tern = 0

    def clean(self):
        print('\n' * 150)

    def start_game(self):
        print("Hello, you are playing for X. Good luck!")
        while True:
            if self.tern % 2 == 0:
                self.print_board()
                print("Player's move")
                print(
                    'Please enter move in format LetterNumber first checker to'
                    ' move and then location (for example A3 A4)')
                move = input()
                move = self.correct_move(move)
                if not move:
                    self.clean()
                    print("Incorrect move try again!")
                    continue
                self.board.make_move(int(move[0][1]) - 1, LETTERS[move[0][0]],
                                     int(move[1][1]) - 1,
                                     LETTERS[move[1][0]])
                self.clean()
            else:
                print("Bot's move")
                print("Thinking, please wait))")
                bot_move(self.board)
                self.clean()
            self.tern += 1
            if self.board.state():
                print("{} won".format(
                    'Bot' if self.board.state() == BLACK else 'Player'))
                self.print_board()
                return 0

    def correct_move(self, move):
        move = move.split()
        if len(move) != 2:
            return None
        mfrom = move[0]
        mto = move[1]

        try:
            if (self.board.get_board()[int(mfrom[1]) - 1][LETTERS.get(
                    mfrom[0])] != WHITE or self.board.get_board()[
                int(mto[1]) - 1][LETTERS.get(mto[0])] != " "):
                return None
        except Exception:
            return None
        if not ((int(mfrom[1]) - int(mto[1]) == 0 and abs(
                LETTERS.get(mfrom[0]) - LETTERS.get(mto[0])) == 1) or (
                        abs(int(mfrom[1]) - int(mto[1])) == 1 and LETTERS.get(
                    mfrom[0]) - LETTERS.get(mto[0]) == 0)):
            return None
        return mfrom, mto

    def print_board(self):
        for i in range(BOARD_SIZE):
            print(i + 1, end=' ')
            for j in range(BOARD_SIZE):
                print(self.board.get_board()[i][j], end=' ')
            print('')
        print('  A B C D')
