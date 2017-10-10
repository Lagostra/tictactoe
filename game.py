from computer_player import ComputerPlayer
import time

def valid_move(move, board):
    if len(move) != 2:
        return False

    if move[0] < 0 or move[0] > len(board) - 1 or move[1] < 0 or move[1] > len(board) - 1:
        return False

    if board[move[1]][move[0]]:
        return False

    return True

def print_board(board):
    for row in board:
        for cell in row:
            print(str(cell) + '\t', end='')
        print()

def game_finished(board, computer_symbol, human_symbol):
    draw = True
    for row in board:
        for cell in row:
            draw &= cell

    if ComputerPlayer.has_won(None, board, computer_symbol):
        print("You lost...")
        return True
    elif ComputerPlayer.has_won(None, board, human_symbol):
        print("You won! Congratulations!")
        return True
    elif draw:
        print("The game ended in a draw...")
        return True

    return False

def play():
    computer_symbol = 2
    human_symbol = 1
    computer_player = ComputerPlayer(computer_symbol, human_symbol)

    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    print_board(board)

    while True:

        if game_finished(board, computer_symbol, human_symbol):
            break

        move = list(map(int, input('Enter your move [x,y]: ').split(',')))
        while not valid_move(move, board):
            print("Invalid move!")
            move = map(int, input('Enter your move [x,y]: '))

        board[move[1]][move[0]] = human_symbol

        print_board(board)

        if game_finished(board, computer_symbol, human_symbol):
            break

        print('Computer is thinking...')
        time.sleep(1)

        move = computer_player.get_best_move(board)
        board[move[1]][move[0]] = computer_symbol

        print_board(board)

if __name__ == '__main__':
    play()