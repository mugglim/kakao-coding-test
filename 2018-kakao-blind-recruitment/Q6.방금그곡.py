import re
import itertools


def to_minute(t):
    hh, mm = map(int, t.split(":"))
    return hh * 60 + mm


def parse(s):
    regex = re.compile("[A-Z]#")
    repl = "?"

    match_list = re.findall(regex, s)

    if not match_list:
        return list(s)

    idx = itertools.count(0)
    return [ch if ch != repl else match_list[idx.__next__()] for ch in re.sub(regex, repl, s)]


def solution(m, musicinfos):
    ans = None

    for musicinfo in musicinfos:
        s, e, title, score = musicinfo.split(",")

        play_minute = to_minute(e) - to_minute(s)
        origin_score = score

        score = parse(score)
        score_len = len(score)
        total_score = ''.join(origin_score) * (play_minute // score_len) + ''.join(score[:play_minute % score_len])

        regex = re.compile(m)

        for match in re.finditer(regex, total_score):
            idx = match.span()[0]
            last_idx = idx + len(m)

            if last_idx >= len(total_score) or total_score[last_idx] != "#":

                if not ans or ans[1] < play_minute:
                    ans = [title, play_minute]
                    break

    return ans[0] if ans else "(None)"
