#imports
import TicTacToeBoard

human = TicTacToeBoard.CROSS
computer = TicTacToeBoard.NOUGHT

def mock_play(board, index, token):
    second_board = board.copy()
    second_board.input_move(index, token)
    return second_board


def computer_AI(board):
    return guess(board)


def guess(board):
    moves = board.free_spaces()

    # Try to win immediately
    for move in moves:
        if mock_play(board, move, computer).win(computer):
            return move

    # Otherwise, try not to lose immediately
    for move in moves:
        if mock_play(board, move, human).win(human):
            return move

    # Otherwise, try to predict how the human player will react to each move
    winning_moves = []
    losing_moves = []
    other_moves = []
    for move in moves:
        human_board = mock_play(board, move, computer)
        (winning_human_moves, blocking_human_moves, other_human_moves) = play_human(human_board)
        if winning_human_moves:
            # The human can win now, the AI should not have played `move`
            losing_moves.append(move)

        elif len(blocking_human_moves) >= 2:
            # The human can block in at least two ways: this means the AI has
            # at least two ways to win. This is perfect!
            winning_moves.append(move)

        else:
            other_moves.append(move)

    if winning_moves:
        return winning_moves[0]
    elif other_moves:
        return other_moves[0]
    else:
        return moves[0]

def play_human(board):
    winning_moves = []
    blocking_moves = []
    other_moves = []
    moves = board.free_spaces()
    if len(moves) > 0:
        for move in board.free_spaces():

            # The human will try to win
            if mock_play(board, move, human).win(human):
                winning_moves.append(move)

            # Otherwise, the human will try not to lose
            elif mock_play(board, move, computer).win(computer):
                blocking_moves.append(move)

            # Otherwise, no move is better
            else:
                other_moves.append(move)
                # TODO: here, the human should try to predict what the computer
                # will do next

    return (winning_moves, blocking_moves, other_moves)
