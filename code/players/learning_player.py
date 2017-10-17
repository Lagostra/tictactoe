import json
import os.path
import random
from collections import defaultdict

from functions import result
from tictactoe_hasher import hash_board


class LearningPlayer:

    LEARNING_DATA_PATH = os.path.join(os.path.dirname(__file__), 'learning_data.json')
    _boards = []
    _board = None

    def __init__(self, board_width=3, board_height=3, board=None, save_each_iteration=True):
        self._save_each_iteration = save_each_iteration
        self.scores = self.load_data(self.LEARNING_DATA_PATH)
        self.reset(board_width, board_height, board)

    def reset(self, board_width=3, board_height=3, board=None):
        if board is None:
            self._board = [[0 for x in range(board_width)] for y in range(board_height)]
        else:
            self._board = board
        self._boards = []

    def get_move(self):
        possible_moves = self.get_possible_moves(self._board)
        random.shuffle(possible_moves)
        best_move = max(possible_moves, key=lambda x: self.scores[hash_board(x[0], False)])

        self._board = best_move[0]
        self._boards.append((self._board, False))

        if result(self._board) != -1:
            self.set_result()

        return best_move[1]


    def opponent_move(self, x, y):
        self._board[y][x] = 2
        self._boards.append((self._board, True))

        if result(self._board) != -1:
            self.set_result()

    def set_result(self):
        if result(self._board) == 2:
            for b in self._boards:
                self.scores[hash_board(b[0], b[1])] -= 5
        elif result(self._board) == 1:
            for b in self._boards:
                self.scores[hash_board(b[0], b[1])] += 5
        elif result(self._board) == 0:
            for b in self._boards:
                self.scores[hash_board(b[0], b[1])] -= 1

        if self._save_each_iteration:
            self.save_data(self.scores, self.LEARNING_DATA_PATH)

    def load_data(self, path):
        if os.path.isfile(path):
            with open(path, 'r') as file:
                return defaultdict(lambda: 0, json.loads(file.read()))
        else:
            return defaultdict(lambda: 0)

    def save_data(self, data, path):
        with open(path, 'w') as file:
            file.write(json.dumps(data))

    def get_possible_moves(self, board):
        moves = []
        for y in range(len(board)):
            for x in range(len(board[0])):
                if not board[y][x]:
                    board_copy = [[board[y][x] for x in range(len(board[0]))] for y in range(len(board))]
                    board_copy[y][x] = 1
                    moves.append((board_copy, (x, y)))
        return moves