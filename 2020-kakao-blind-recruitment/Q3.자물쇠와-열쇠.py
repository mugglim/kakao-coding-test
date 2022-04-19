def rotate90(arr):
    n = len(arr)
    return [[arr[i][-1-j] for i in range(n)] for j in range(n)]


def solution(key, lock):
    m, n = len(key), len(lock)
    lock_size = n*n
    board_size = n + (m-1) * 2
    board = [[0] * board_size for _ in range(board_size)]

    def attach(y, x, key):
        for ny in range(y, y+m):
            for nx in range(x, x+m):
                board[ny][nx] += key[ny-y-m][nx-x-m]

    def detach(y, x, key):
        for ny in range(y, y+m):
            for nx in range(x, x+m):
                board[ny][nx] -= key[ny-y-m][nx-x-m]

    def is_open():
        return len([True for i in range(m-1, m+n-1) for j in range(m-1, m+n-1) if board[i][j] == 1]) == lock_size

    def init_board():
        for i in range(m, m+n):
            for j in range(m, m+n):
                board[i-1][j-1] = lock[i-m][j-m]

    def chk():
        for y in range(m+n-1):
            for x in range(m+n-1):
                attach(y, x, key)
                if is_open():
                    return True
                detach(y, x, key)

        return False

    init_board()

    for k in range(4):
        if k > 0:
            key = rotate90(key)

        if chk():
            return True

    return False
