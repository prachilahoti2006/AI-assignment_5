import math

game_board = [
    'X', 'X', ' ',
    'O', ' ', ' ',
    ' ', 'O', ' '
]

def board_score(state):

    score = 0

    winning_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for line in winning_lines:

        symbols = [state[pos] for pos in line]

        if symbols.count('X') == 2 and symbols.count(' ') == 1:
            score += 10

        elif symbols.count('O') == 2 and symbols.count(' ') == 1:
            score -= 10

    return score


def alpha_beta(state, level, alpha, beta, is_max):

    if level == 0:
        return board_score(state)

    if is_max:

        max_score = -math.inf

        for pos in range(len(state)):

            if state[pos] == ' ':

                state[pos] = 'X'

                current_score = alpha_beta(
                    state,
                    level - 1,
                    alpha,
                    beta,
                    False
                )

                max_score = max(max_score, current_score)

                state[pos] = ' '

                alpha = max(alpha, max_score)

                if alpha >= beta:
                    break

        return max_score

    else:

        min_score = math.inf

        for pos in range(len(state)):

            if state[pos] == ' ':

                state[pos] = 'O'

                current_score = alpha_beta(
                    state,
                    level - 1,
                    alpha,
                    beta,
                    True
                )

                min_score = min(min_score, current_score)

                state[pos] = ' '

                beta = min(beta, min_score)

                if alpha >= beta:
                    break

        return min_score


result = alpha_beta(
    game_board,
    3,
    -math.inf,
    math.inf,
    True
)

print("Heuristic Score:", result)
