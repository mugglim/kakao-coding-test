from bisect import bisect_left
from itertools import product

QUERY_INFO_LIST = [
    ['cpp', 'java', 'python'],
    ['frontend', 'backend'],
    ['junior', 'senior'],
    ['chicken', 'pizza']
]


def count_greater_of(sorted_arr, val):
    return len(sorted_arr) - bisect_left(sorted_arr, val)


def solution(info, query):
    score_document = {}
    score_cache = {}
    ans = []

    # init scheme
    for props in product(*QUERY_INFO_LIST):
        curr = score_document
        for prop in props:
            if prop not in curr:
                if prop != props[-1]:
                    curr[prop] = {}
                else:
                    curr[prop] = []
            curr = curr[prop]

    # insert score
    for l in info:
        infos = l.split(" ")
        props, score = infos[:-1], int(infos[-1])
        curr = score_document

        for prop in props:
            if prop not in curr:
                if prop != props[-1]:
                    curr[prop] = {}
                else:
                    curr[prop] = []
            curr = curr[prop]

        score_list_id = id(curr)

        if score_list_id not in score_cache:
            score_cache[score_list_id] = curr

        curr.append(score)

    # sort score by asc
    for score_list in score_cache.values():
        score_list.sort()

    # handle query
    for q in query:
        infos = q.replace("and ", "").split(" ")

        props_list = [[infos[i]] if prop != "-" else QUERY_INFO_LIST[i]
                      for i, prop in enumerate(infos[:-1])]
        score = int(infos[-1])
        cnt = 0

        for props in list(product(*props_list)):
            curr = score_document

            for prop in props:
                curr = curr[prop]

            cnt += count_greater_of(curr, score)

        ans.append(cnt)

    return ans
