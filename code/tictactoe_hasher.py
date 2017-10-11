def hash_board(board, player_moving):
    '''
    Calculates a perfect hash value for a tic-tac-toe board
    :param board: Rectangular 2D array representing the tic-tac-toe board, with cell state represented by 0, 1 or 2
    :param player_moving: Is the player moving next? (False if opponent is moving next)
    :return: Hash value of the board
    '''
    sum = 0

    for y in range(len(board)):
        for x in range(len(board[0])):
            sum += board[y][x] * 3**(len(board[0]) * y + x)

    sum += player_moving * 3**(len(board) * len(board[0]))
    return sum

def convert(board, symbol1, symbol2, symbol3):
    '''
    Converts a board in a format with symbols other than 0, 1 and 2 representing cell state. Which symbols represent
    what does not affect functionality.
    :param board: Rectangular 2D array representing the tic-tac board.
    :param symbol1: The first symbol. Will be converted to 0.
    :param symbol2: The second symbol. Will be converted to 1.
    :param symbol3: The third symbol. Will be converted to 2.
    :return: Converted board
    '''

    new_board = []
    for y in range(len(board)):
        new_board.append([])
        for x in range(len(board[0])):
            if board[y][x] == symbol1:
                new_board[y].append(0)
            elif board[y][x] == symbol2:
                new_board[y].append(1)
            elif board[y][x] == symbol3:
                new_board[y].append(2)
            else:
                new_board[y].append(None)

    return new_board