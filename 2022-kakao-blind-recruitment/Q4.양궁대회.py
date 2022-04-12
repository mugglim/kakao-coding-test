from itertools import combinations_with_replacement as cwp


def to_info(max_score, arrow_info):
    info = [0 for i in range(max_score + 1)]
    for arrow in arrow_info:
        info[max_score - arrow] += 1
    return info


def solution(n, info):
    max_score = len(info) - 1
    ans = [-1, []]
    line_info_list = list([to_info(max_score, arrow_info)
                          for arrow_info in cwp([i for i in range(max_score + 1)], n)])

    for line_info in line_info_list:
        score_list = [0, 0]  # 라이언, 아파치 점수

        # 점수 계산
        for i, [line_count, apache_count] in enumerate(zip(line_info, info)):
            # 모두 화살을 맞히지 못한 점수
            if line_count == apache_count and line_count == 0:
                continue

            if line_count > apache_count:
                score_list[0] += (max_score - i)
            else:
                score_list[1] += (max_score - i)

        # 라이언이 경기를 이긴 경우
        score_diff = score_list[0] - score_list[1]
        if score_diff > 0 and score_diff > ans[0]:
            ans = [score_diff, line_info]

    return [-1] if ans[0] == -1 else ans[1]
