# "hh:mm"(string) to minute(int)
def minute_of(formatted_time):
    h, m = map(int, formatted_time.split(":"))
    return h * 60 + m


# minute(int) to "hh:mm"(string)
def format_of(minute_time):
    hh = minute_time // 60
    mm = minute_time % 60
    return f"{hh:02d}:{mm:02d}"


def solution(n, t, m, timetable):
    ans = ""
    
    bus_time_list = [minute_of("09:00") + t * i for i in range(n)]
    user_time_list = [minute_of(_time) for _time in sorted(timetable)]
    user_time_idx = 0

    for bus_time_idx, bus_time in enumerate(bus_time_list):
        cnt = 0  # 탑승한 승객

        # 현재 bus_time 탑승할 수 있는 승객 카운팅
        for user_time in user_time_list[user_time_idx:user_time_idx+m]:
            if user_time <= bus_time:
                cnt += 1

        # 탑승한 승객 번호 반영
        user_time_idx += cnt

        # 마지막 버스 시간대라면
        if bus_time_idx == len(bus_time_list) - 1:

            # 승객 m명이 모두 탑승한 경우
            if cnt == m:
                last_user_idx = user_time_idx - 1  # same as (previous_user_time_idx + cnt(m) - 1)
                ans = user_time_list[last_user_idx] - 1  # 마지막 승객보다 1분 빨리 오면 됨
            else:
                ans = bus_time  # 그냥 버스 시간에 타면 됨

    return format_of(ans)
