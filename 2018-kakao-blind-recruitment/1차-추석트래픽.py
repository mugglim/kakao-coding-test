def line_to_ms(line):
    d, t, diff_s = line.split(' ')

    h, m, float_s = t.split(":")
    s, ms = float_s.split(".")
    diff_s = diff_s.split('s')[0]

    h_ms = int(h) * 3600 * 1000
    m_ms = int(m) * 60 * 1000
    s_ms = int(s) * 1000
    ms = int(ms)
    diff_ms = int(float(diff_s) * 1000)

    end_ms = h_ms + m_ms + s_ms + ms
    start_ms = end_ms - diff_ms + 1  # 시작 시간 포함

    return [start_ms, end_ms]


def count_overlap(t, line_ms_list):
    cnt = 0

    def is_ovelap(s1, e1, s2, e2): return s1 <= e2 and e1 >= s2

    for [start_ms, end_ms] in line_ms_list:
        if is_ovelap(t, t+999, start_ms, end_ms):
            cnt += 1

    return cnt


def solution(lines):
    n = len(lines)
    ans = 0
    line_ms_list = list(map(line_to_ms, lines))

    for [start_ms, end_ms] in line_ms_list:
        ans = max(ans, count_overlap(start_ms, line_ms_list),
                  count_overlap(end_ms, line_ms_list))

    return ans
