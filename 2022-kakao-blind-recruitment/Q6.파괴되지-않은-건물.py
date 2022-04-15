# for imos
D_ATTACK = [-1, 1, 1, -1]
D_DEFEND = [1, -1, -1, 1]


def solution(board, skill):
    n, m = len(board), len(board[0])
    prefix = [[0] * m for _ in range(n)]

    def chk(y, x):
        return 0 <= y < n and 0 <= x < m

    for [type_opt, r1, c1, r2, c2, degree] in skill:

        for i, [y, x] in enumerate([(r1, c1), (r1, c2+1), (r2+1, c1), (r2+1, c2+1)]):
            d_degree = degree * (D_ATTACK[i] if type_opt == 1 else D_DEFEND[i])

            if chk(y, x):
                prefix[y][x] += d_degree

    # sweep to width
    for i in range(n):
        for j in range(1, m):
            prefix[i][j] += prefix[i][j-1]

    # sweep to height
    for j in range(m):
        for i in range(1, n):
            prefix[i][j] += prefix[i-1][j]

    # count not destroyed
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + prefix[i][j] > 0:
                cnt += 1

    return cnt
