from collections import deque

dx = [0, 1, 0, 1]
dy = [0, 0, 1, 1]


def solution(m, n, board):
    cnt = 0
    board = [list(row) for row in board]

    def chk(i, j):
        if not board[i][j]:
            return False
        if i+1 >= m or j+1 >= n:
            return False
        return board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]

    def move():
        for j in range(n):
            for i in range(m-2, -1, -1):
                k = i
                while k+1 < m and board[k][j] and not board[k+1][j]:
                    board[k][j], board[k+1][j] = board[k+1][j], board[k][j]
                    k += 1

    while True:
        pop_dic = {}

        for i in range(m-1):
            for j in range(n-1):
                if chk(i, j):
                    for k in range(4):
                        ni, nj = i+dy[k], j+dx[k]
                        pop_dic[(ni, nj)] = True

        if not pop_dic:
            break

        for (i, j) in pop_dic.keys():
            board[i][j] = ''

        cnt += len(pop_dic)
        move()

    return cnt
