from minimax_player import MinimaxPlayer
from maximize_sum_player import MaximizeSumPlayer
from functions import print_board
from functions import result
import time


def valid_move(move, board):
    if len(move) != 2:
        return False

    if move[0] < 0 or move[0] > len(board) - 1 or move[1] < 0 or move[1] > len(board) - 1:
        return False

    if board[move[1]][move[0]]:
        return False

    return True


def game_finished(board, computer_symbol, human_symbol):
    res = result(board)
    if res == 2:
        print("You lost...")
        return True
    elif res == 1:
        print("You won! Congratulations!")
        return True
    elif res == 0:
        print("The game ended in a draw...")
        return True

    return False

def play():
    computer_symbol = 2
    human_symbol = 1
    computer_player = MinimaxPlayer(3, 3)

    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    print_board(board)

    player_starting = True

    while True:

        if game_finished(board, computer_symbol, human_symbol):
            break

        if player_starting:
            move = list(map(int, input('Enter your move [x,y]: ').split(',')))
            while not valid_move(move, board):
                print("Invalid move!")
                move = map(int, input('Enter your move [x,y]: '))

            board[move[1]][move[0]] = human_symbol
            computer_player.opponent_move(move[0], move[1])
            print_board(board)

            if game_finished(board, computer_symbol, human_symbol):
                break

        print('Computer is thinking...')
        time.sleep(1)

        move = computer_player.get_move()
        board[move[1]][move[0]] = computer_symbol

        print_board(board)

        if game_finished(board, computer_symbol, human_symbol):
            break

        player_starting = True

if __name__ == '__main__':
    play()