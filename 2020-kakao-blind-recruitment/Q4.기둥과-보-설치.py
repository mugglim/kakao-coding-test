def solution(n, build_frame):
    board = [[[False]*(2) for _ in range(n+1)] for _ in range(n+1)]

    def chk_column(y, x):
        if y == 0:
            return True
        if board[y-1][x][0]:
            return True
        if (x > 0 and board[y][x-1][1]) or board[y][x][1]:
            return True
        return False

    def chk_beam(y, x):
        if board[y-1][x][0] or board[y-1][x+1][0]:
            return True
        if x > 0 and board[y][x-1][1] and board[y][x+1][1]:
            return True
        return False

    def chk_board():
        for y in range(n+1):
            for x in range(n+1):
                if board[y][x][0] and not chk_column(y, x):
                    return False
                if board[y][x][1] and not chk_beam(y, x):
                    return False

        return True

    for [x, y, a, b] in build_frame:
        if b == 1:  # 추가
            board[y][x][a] = True
            if a == 0 and not chk_column(y, x):
                board[y][x][a] = False
            if a == 1 and not chk_beam(y, x):
                board[y][x][a] = False
        if b == 0:  # 삭제
            board[y][x][a] = False
            if not chk_board():
                board[y][x][a] = True

    res = [[x, y, k]for y in range(n+1) for x in range(n+1) for k in range(2) if board[y][x][k]]
    res.sort(key=lambda x: (x[0:]))

    return res
