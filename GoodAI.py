import random
import TicTacToeBoard


def computer_AI(board):

    # If possible, win immediately
    for i in range(0,9):
        if board.is_free(i):
            copied_board = board.copy()
            copied_board.input_move(i, TicTacToeBoard.NOUGHT)
            if copied_board.win(TicTacToeBoard.NOUGHT):
                return i

    # Prevent player from winning immediately
    for i in range(0,9):
        if board.is_free(i):
            copied_board = board.copy()
            copied_board.input_move(i, TicTacToeBoard.CROSS)
            if copied_board.win(TicTacToeBoard.CROSS):
                return i

    if board.is_free(4):
        return 4
    move = choose_move_from_list(board, [0,2,6,8])
    if move is not None:
        return move
    move = choose_move_from_list(board, [1,3,5,7])
    if move is not None:
        return move

def choose_move_from_list(board, moves_list):
    #Randomly select a value from a list of values
    possible_moves = []
    for i in moves_list:
        if board.is_free(i):
            possible_moves.append(i)

    if len(possible_moves) > 0:
        return random.choice(possible_moves)
