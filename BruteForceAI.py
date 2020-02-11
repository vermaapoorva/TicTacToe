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
    second_board = board.copy()
    second_board.input_move(index, token)
    return second_board



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

    # wins, draws, and loses holds the winning, drawing and losing moves. They
    # are filled below.
    wins = []
    draws = []
    loses = []

    # the available moves are each inspected one by one.
    available_moves = board.free_spaces()
    for move in available_moves:
        # each move is
        # FIRST: simulated
        possible_board = mock_play(board, move, TicTacToeBoard.CROSS)

        # SECOND: check whether this leads to victory or draw
        outcome = outcome_of_board(possible_board)
        if outcome == CROSSWIN:
            wins.append(move)
        elif outcome == DRAW:
            draws.append(move)
        else:
            # If it does not lead to victory or draw, it depends on what the
            # other player will do with the board.

            # THIRD: the result of the simulated move is passed to the opponent
            (nought_wins, nought_draws, nought_loses) = nought_play(possible_board)

            # FOURTH: the opponents opportunities are analysed
            # If the opponent can win, it means we lose when playing this move
            if nought_wins:
                loses.append(move)
            # If the opponent cannot win but can draw it means we draw
            elif nought_draws:
                draws.append(move)
            # If the opponent cannot win nor draw it means we are assured victory!
            elif nought_loses:
                wins.append(move)

    # We return the result of this play
    return (wins, draws, loses)

def nought_play(board):
    wins = []
    draws = []
    loses = []
    available_moves = board.free_spaces()
    for move in available_moves:
        possible_board = mock_play(board, move, TicTacToeBoard.NOUGHT)
        outcome = outcome_of_board(possible_board)
        if outcome == NOUGHTWIN:
            wins.append(move)
        elif outcome == DRAW:
            draws.append(move)
        else:
            (cross_wins, cross_draws, cross_loses) = cross_play(possible_board)
            if cross_wins:
                loses.append(move)
            elif cross_draws:
                draws.append(move)
            elif cross_loses:
                wins.append(move)
    return (wins, draws, loses)

