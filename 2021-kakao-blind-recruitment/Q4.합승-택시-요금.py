import sys
INF = sys.maxsize


def solution(n, s, a, b, fares):
    costs = [[INF] * (n+1) for _ in range(n+1)]
    ans = INF

    for [i, j, cost] in fares:
        costs[i][j], costs[j][i] = cost, cost

    for i in range(1, n+1):
        costs[i][i] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

    for k in range(1, n+1):
        ans = min(
            ans,
            costs[s][k] + costs[k][a] + costs[k][b],
            costs[s][a] + costs[s][b]
        )

    return ans
