def second_of(format_time):
    h, m, s = map(int, format_time.split(":"))
    return h * 3600 + m * 60 + s


def format_of(second):
    result = []
    quotient_list = [3600, 60, 1]

    for quotient in quotient_list:
        result.append(f"{second // quotient:02d}")
        second %= quotient

    return ':'.join(result)


def solution(play_time, adv_time, logs):
    play_time_sec = second_of(play_time)
    adv_time_sec = second_of(adv_time)
    prefix = [0 for i in range(play_time_sec + 1)]

    for log in logs:
        start_time, end_time = log.split('-')
        start_time_sec = second_of(start_time)
        end_time_sec = second_of(end_time)

        prefix[start_time_sec] += 1  # 시작 시각
        prefix[end_time_sec] -= 1  # 종료 시각

    # 누적합을 2번 수행하여, '0'인 구간에 시청자 수 반영
    for i in range(1, play_time_sec + 1):
        prefix[i] += prefix[i-1]

    for i in range(1, play_time_sec + 1):
        prefix[i] += prefix[i-1]

    # prefix [0,adv_time_sec] 구간의 시청자수는 최소 누적 시청자 수
    ans = [0, prefix[adv_time_sec]]

    # prefix는 idx 1부터 시작
    for sec in range(adv_time_sec + 1, play_time_sec+1):
        cnt = prefix[sec] - prefix[sec - adv_time_sec]
        start_sec = sec - adv_time_sec + 1

        if cnt > ans[1]:
            ans = [start_sec, cnt]

    return format_of(ans[0])
