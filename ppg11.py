#alpha beta pruning
import math
def alpha_beta(depth, nodeIndex, maximizingPlayer, values, height, alpha, beta):
    if depth == height:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, False, values, height, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, True, values, height, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best