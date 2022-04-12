D_STRAIGHT_1 = [[-1, 0], [1, 0], [0, -1], [0, 1]]
D_STRAIGHT_2 = [[-2, 0], [2, 0], [0, -2], [0, 2]]
D_DIAGONAL_2 = [[-1, -1], [-1, 1], [1, 1], [1, -1]]


def chk(place):

    def is_out_of_bounds(y, x):
        return y < 0 or y >= 5 or x < 0 or x >= 5

    def is_continue(y, x):
        return is_out_of_bounds(y, x) or place[y][x] != "P"

    for y in range(5):
        for x in range(5):
            if place[y][x] != "P":
                continue

            # 직선 거리 1
            for [dy, dx] in D_STRAIGHT_1:
                ny, nx = y+dy, x+dx
                if is_continue(ny, nx):
                    continue

                return 0

            # 직선 거리 2
            for [dy, dx] in D_STRAIGHT_2:
                ny, nx = y+dy, x+dx
                if is_continue(ny, nx):
                    continue

                # y 좌표가 달라진 경우
                if ny != y and place[(y+ny) // 2][nx] != "X":
                    return 0

                # x 좌표가 달라진 경우
                if nx != x and place[ny][(nx+x) // 2] != "X":
                    return 0

            # 대각선 거리 2
            for [dy, dx] in D_DIAGONAL_2:
                ny, nx = y+dy, x+dx
                if is_continue(ny, nx):
                    continue

                if place[ny][x] != "X" or place[y][nx] != "X":
                    return 0

    return 1


def solution(places):
    ans = []

    for place in places:
        ans.append(chk(place))

    return ans
