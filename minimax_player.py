from tictactoe_hasher import hash_board
from functions import result
from functions import print_board

class MinimaxPlayer:

    draws = 0
    wins = 0
    losses = 0

    def __init__(self, board_width=3, board_height=3, board=None):
        self._scores = [None for i in range(3 ** (board_width * board_height + 1))]
        if board is None:
            self._board = [[0 for x in range(board_width)] for y in range(board_height)]
        else:
            self._board = board

    def get_move(self):
        best_move = None
        best_score = None

        for move in self.get_possible_moves(self._board):
            score = self.get_score(move[0], False)
            if best_score is None or score > best_score:
                best_score = score
                best_move = move[1]

        self._board[best_move[1]][best_move[0]] = 1
        return best_move

    def opponent_move(self, x, y):
        self._board[y][x] = 2

    def get_score(self, board, player_moving=True, depth=0):
        hash = hash_board(board, player_moving)

        if self._scores[hash] is not None:
            return self._scores[hash]

        res = result(board)
        if res == 1:
            self.wins += 1
            self._scores[hash] = 100 - depth
            return 100 - depth
        if res == 2:
            self.losses += 1
            self._scores[hash] = depth - 100
            return depth - 100
        if res == 0:
            self.draws += 1
            self._scores[hash] = 0
            return 0

        possible_moves = self.get_possible_moves(board, player_moving)

        best_score = None
        for move in possible_moves:
            score = self.get_score(move[0], not player_moving, depth + 1)
            if best_score is None \
                    or ((player_moving and score > best_score)
                        or (not player_moving and score < best_score)):
                best_score = score

        self._scores[hash] = best_score
        return best_score

    def get_possible_moves(self, board, player_moving=True):
        moves = []
        for y in range(len(board)):
            for x in range(len(board[0])):
                if not board[y][x]:
                    board_copy = [[board[y][x] for x in range(len(board[0]))] for y in range(len(board))]
                    board_copy[y][x] = 1 if player_moving else 2
                    moves.append((board_copy, (x, y)))
        return moves
