import re
from functools import reduce


def go(*functions):
    return reduce(lambda x, f: f(x), functions)


def solution(new_id):
    return go(
        new_id,
        lambda id: id.lower(),
        lambda id: re.sub('[^a-z\d_.-]', '', id),
        lambda id: re.sub('\.{2,}', '.', id),
        lambda id: re.sub('(^\.|\.$)', '', id),
        lambda id: 'a' if not id else id,
        lambda id: re.sub("\.$", '', id[:15]),
        lambda id: id if len(id) >= 3 else id + id[-1] * (3 - len(id))
    )
