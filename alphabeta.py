import math

def alpha_beta_search(level, index, is_max_player, scores, alpha, beta):

    if level == 3:
        return scores[index]

    if is_max_player:
        max_value = -math.inf

        for child in range(2):
            current = alpha_beta_search(
                level + 1,
                index * 2 + child,
                False,
                scores,
                alpha,
                beta
            )

            max_value = max(max_value, current)
            alpha = max(alpha, max_value)

            if alpha >= beta:
                break

        return max_value

    else:
        min_value = math.inf

        for child in range(2):
            current = alpha_beta_search(
                level + 1,
                index * 2 + child,
                True,
                scores,
                alpha,
                beta
            )

            min_value = min(min_value, current)
            beta = min(beta, min_value)

            if alpha >= beta:
                break

        return min_value


leaf_nodes = [3, 5, 6, 9, 1, 2, 0, -1]

optimal_result = alpha_beta_search(
    0,
    0,
    True,
    leaf_nodes,
    -math.inf,
    math.inf
)

print("Optimal Value:", optimal_result)
