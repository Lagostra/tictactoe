def has_won(board, player_symbol):
    '''
    Returns true if the given board represents a victory for specified player; false otherwise
    :param board: 2D array representing the board
    :param player_symbol: The symbol of the player to be checked for victory
    :return: Whether or not the player has won on the given board
    '''

    # Check rows
    for y in range(len(board)):
        won = True
        for x in range(len(board[y])):
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
        if board[-i - 1][i] != player_symbol:
            won2 = False

    return won or won2

def result(board):
    '''
    Returns the result of the given board
    :param board: 2D array representing the board
    :return: 0 if the board represents a draw, 1 if player 1 has won, 2 if player 2 has won,
            -1 if the game is not finished
    '''

    if has_won(board, 1):
        return 1
    if has_won(board, 2):
        return 2

    for row in board:
        for cell in row:
            if cell == 0:
                return -1

    return 0

def print_board(board):
    for row in board:
        for cell in row:
            print(str(cell) + '\t', end='')
        print()
    print()
