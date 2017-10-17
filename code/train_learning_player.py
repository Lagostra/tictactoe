from functions import result
from players.learning_player import LearningPlayer
from players.random_player import RandomPlayer
from players.minimax_player import MinimaxPlayer

def valid_move(board, move):
    if len(move) != 2:
        return False

    if move[0] < 0 or move[0] > len(board) - 1 or move[1] < 0 or move[1] > len(board) - 1:
        return False

    if board[move[1]][move[0]]:
        return False

    return True


def play_single_game(players, player_moving = 0):
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    while result(board) == -1:
        move = players[player_moving].get_move()

        if valid_move(board, move):
            board[move[1]][move[0]] = player_moving + 1
            next_player = (player_moving + 1) % 2
            players[next_player].opponent_move(move[0], move[1])
            player_moving = next_player

if __name__ == '__main__':
    players = (MinimaxPlayer(), LearningPlayer(save_each_iteration=False))

    for i in range(1000000):
        play_single_game(players, i % 2)
        if not i % 1000:
            print(i, 'iterations completed')
            players[1].save_data(players[1].scores, players[1].LEARNING_DATA_PATH)
        for p in players:
            p.reset()