import copy

class ComputerPlayer:

    _scores = {}

    def __init__(self, player_symbol=1, opponent_symbol=2):
        self._player_symbol = player_symbol
        self._opponent_symbol = opponent_symbol

    def get_best_move(self, board):
        return self.get_score(board)[1]

    def get_score(self, board, maximize = True):
        if board in self._scores:
            return self._scores[board]

        if self.has_won(board, self._player_symbol):
            return 1
        if self.has_won(board, self._opponent_symbol):
            return -1

        possible_moves = self.get_possible_moves(board)

        # No possible moves, not loss or win -> draw
        if len(possible_moves) == 0:
            return 0

        best_score = self.get_score(possible_moves[0][0], not maximize)
        best_move = 0
        for i in range(1, len(possible_moves)):
            move_score = self.get_score(possible_moves[i], not maximize)
            if (maximize and move_score > best_score) or (not maximize and move_score < best_score):
                best_score = move_score
                best_move = i

        return best_score, possible_moves[best_move][1]

    def get_possible_moves(self, board):
        moves = []

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] is None:
                    board_copy = copy.deepcopy(board)
                    board_copy[y][x] = self._player_symbol
                    moves.append((board_copy, (x, y)))

        return moves
    def has_won(self, board, player_symbol):
        # Check rows
        for y in range(len(board)):
            won = True
            for x in range(len(board[0])):
                if board[y][x] != player_symbol:
                    won = False
                    break
            if won:
                break

        if won:
            return True

        # Check columns
        for x in range(len(board[0])):
            won = True
            for y in range(len(board)):
                if board[y][x] != player_symbol:
                    won = False
                    break
            if won:
                break

        if won:
            return True

        # Check diagonals
        won = True
        won2 = True
        for i in range(len(board)):
            if board[i][i] != player_symbol:
                won = False
            if board[-i-1][i] != player_symbol:
                won2 = False

        return won or won2