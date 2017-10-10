def hash(board):
    '''
    Calculates a perfect hash value for a tic-tac-toe board
    :param board: Rectangular 2D array representing the tic-tac-toe board, with cell state represented by 0, 1 or 2
    :return: Hash value of the board
    '''
    sum = 0

    for y in len(board):
        for x in len(board[0]):
            sum += board[y][x] * 3**(len(board[0]) * y + x)

    return sum