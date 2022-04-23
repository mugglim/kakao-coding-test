def can_jump(stones, mid, k):
    cnt = 0

    for stone in stones:
        if stone <= mid:
            # 만약 연속되는 0의 개수가 k랑 같다면 더 이상 이동할 수 없음
            if cnt + 1 == k:
                return False

            # 아닌 경우에는 카운팅 해준다.
            cnt += 1
        else:
            cnt = 0

    return True


def solution(stones, k):
    l = 1
    r = max(stones)

    while l <= r:
        # 한 번에 mid 명이 이동한다.
        mid = (l+r) // 2

        if can_jump(stones, mid, k):
            # 한 번에 이동하는 인원을 늘린다.
            l = mid + 1
        else:
            # 한 번에 이동하는 인원을 줄인다.
            r = mid - 1

    return l
