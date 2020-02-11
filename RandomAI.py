import random


def computer_AI(board):
    possible_moves = []
    for i in range(0,8):
        if board.is_free(i):
            possible_moves.append(i)

    return random.choice(possible_moves)

