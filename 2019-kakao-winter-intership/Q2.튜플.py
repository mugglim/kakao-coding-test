import re
from functools import reduce


def go(*functions):
    return reduce(lambda x, f: f(x), functions)


def flatten2D(arr):
    return [el for row in arr for el in row]


def solution(s):
    num_list = go(
        s,
        lambda x: x[1:-1],
        lambda x: x.split("},"),
        lambda l: sorted(l, key=lambda x: len(x)),
        lambda l: list(map(lambda x: re.sub("[{}]", '', x), l)),
        lambda l: list(map(lambda x: x.split(","), l)),
        lambda l: flatten2D(l)
    )

    return list(map(int, dict.fromkeys(num_list)))
