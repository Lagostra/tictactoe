import random

class RandomPlayer:

    def __init__(self, board_width=3, board_height=3, board=None):
        if board is None:
            self._board = [[0 for x in range(board_width)] for y in range(board_height)]
        else:
            self._board = board

    def get_move(self):

        possible_moves = []
        for y in range(len(self._board)):
            for x in range(len(self._board[0])):
                if self._board[y][x] == 0:
                    possible_moves.append((x, y))

        move = random.choice(possible_moves)
        self._board[move[1]][move[0]] = 1
        return move

    def opponent_move(self, x, y):
        self._board[y][x] = 2
