import math

game_state = [' ' for _ in range(9)]

winning_patterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def display_board(state):
    for row in range(0, 9, 3):
        print(state[row:row + 3])

def winner_exists(state, symbol):
    for pattern in winning_patterns:
        if all(state[pos] == symbol for pos in pattern):
            return True
    return False

def board_full(state):
    return ' ' not in state

def evaluate_move(state, is_max_turn):

    if winner_exists(state, 'X'):
        return 1

    if winner_exists(state, 'O'):
        return -1

    if board_full(state):
        return 0

    if is_max_turn:

        max_score = -math.inf

        for pos in range(9):
            if state[pos] == ' ':
                state[pos] = 'X'

                score = evaluate_move(state, False)

                max_score = max(max_score, score)

                state[pos] = ' '

        return max_score

    else:

        min_score = math.inf

        for pos in range(9):
            if state[pos] == ' ':
                state[pos] = 'O'

                score = evaluate_move(state, True)

                min_score = min(min_score, score)

                state[pos] = ' '

        return min_score

def find_best_move(state):

    highest_score = -math.inf
    best_position = -1

    for pos in range(9):

        if state[pos] == ' ':

            state[pos] = 'X'

            current_score = evaluate_move(state, False)

            state[pos] = ' '

            if current_score > highest_score:
                highest_score = current_score
                best_position = pos

    return best_position

game_state = [
    'X', 'X', ' ',
    'O', 'O', ' ',
    ' ', ' ', ' '
]

print("Best Move:", find_best_move(game_state))
