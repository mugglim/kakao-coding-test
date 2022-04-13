import sys
from collections import deque

INF = sys.maxsize
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(board):
    n = len(board)
    ans = INF

    # y,x,cost,dir
    queue = deque([(0, 0, 0, -1)])
    costs = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    def chk(y, x):
        return y < 0 or y >= n or x < 0 or x >= n

    while queue:
        y, x, cost, _dir = queue.popleft()

        if y == n-1 and x == n-1:
            ans = min(cost, ans)

        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]

            if chk(ny, nx) or (ny == 0 and nx == 0):
                continue

            new_cost = cost + (100 if _dir == -1 or _dir == k else 600)

            if board[ny][nx] == 0 and new_cost < costs[ny][nx][k]:
                costs[ny][nx][k] = new_cost
                queue.append((ny, nx, new_cost, k))

    return ans
