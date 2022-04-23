import re
import math
from functools import reduce
from collections import Counter


def go(*fns):
    return reduce(lambda x, f: f(x), fns)


def counter_union(c1, c2):
    cnt = 0

    for p1 in c1:
        if p1 in c2:
            cnt += max(c1[p1], c2[p1])
        else:
            cnt += c1[p1]

    for p2 in c2:
        if p2 not in c1:
            cnt += c2[p2]

    return cnt


def counter_intersection(c1, c2):
    cnt = 0

    for p1 in c1:
        if p1 in c2:
            cnt += min(c1[p1], c2[p1])

    return cnt


def split_of(s, n=2):
    return go(
        [s[i:i+n] for i in range(len(s)-n+1)],
        lambda l: filter(lambda word: not re.findall('[^a-zA-Z]', word), l),
        lambda l: list(l)
    )


def solution(str1, str2):
    counter1 = Counter(split_of(str1.lower()))
    counter2 = Counter(split_of(str2.lower()))

    union_cnt = counter_union(counter1, counter2)
    intersection_cnt = counter_intersection(counter1, counter2)

    ans = intersection_cnt / union_cnt if union_cnt > 0 else 1

    return math.floor(65536 * ans)
