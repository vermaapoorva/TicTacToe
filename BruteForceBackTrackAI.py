import TicTacToeBoard

CROSSWIN = 1
DRAW = 2
NOUGHTWIN = 3

def outcome_of_board(board):
    if board.win(TicTacToeBoard.CROSS):
        return CROSSWIN
    if board.win(TicTacToeBoard.NOUGHT):
        return NOUGHTWIN
    if board.full():
        return DRAW
    return None

def mock_play(board, index, token):
    board.input_move(index, token)
def unmock_play(board, index):
    board.input_move(index, None)



def computer_AI(board, token):

    # Play the appropriate token
    if token == TicTacToeBoard.CROSS:
        (winning_moves, drawing_moves, losing_moves) = cross_play(board)
    else:
        (winning_moves, drawing_moves, losing_moves) = nought_play(board)

    #Choose amongst the best moves available
    if winning_moves:
        return winning_moves[0]
    elif drawing_moves:
        return drawing_moves[0]
    elif losing_moves:
        return drawing_moves[0]
    else:
        return None


def cross_play(board):
    wins = []
    draws = []
    loses = []
    available_moves = board.free_spaces()
    for move in available_moves:
        mock_play(board, move, TicTacToeBoard.CROSS)
        outcome = outcome_of_board(board)
        if outcome == CROSSWIN:
            wins.append(move)
        elif outcome == DRAW:
            draws.append(move)
        else:
            (nought_wins, nought_draws, nought_loses) = nought_play(board)
            if nought_wins:
                loses.append(move)
            elif nought_draws:
                draws.append(move)
            elif nought_loses:
                wins.append(move)
        unmock_play(board, move)
    return (wins, draws, loses)

def nought_play(board):
    wins = []
    draws = []
    loses = []
    available_moves = board.free_spaces()
    for move in available_moves:
        mock_play(board, move, TicTacToeBoard.NOUGHT)
        outcome = outcome_of_board(board)
        if outcome == NOUGHTWIN:
            wins.append(move)
        elif outcome == DRAW:
            draws.append(move)
        else:
            (cross_wins, cross_draws, cross_loses) = cross_play(board)
            if cross_wins:
                loses.append(move)
            elif cross_draws:
                draws.append(move)
            elif cross_loses:
                wins.append(move)
        unmock_play(board, move)
    return (wins, draws, loses)

