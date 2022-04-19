from bisect import bisect_left, bisect_right


def range_of(arr, a, b):
    return bisect_right(arr, b) - bisect_left(arr, a)


def solution(words, queries):
    word_dic = {}
    ans = []

    for word in words:
        size = len(word)

        if size not in word_dic:
            word_dic[size] = {
                'l': [],
                'r': []
            }

        word_dic[size]['l'].append(word)
        word_dic[size]['r'].append(word[::-1])

    for k in word_dic.keys():
        word_dic[k]['l'].sort()
        word_dic[k]['r'].sort()

    for query in queries:
        size = len(query)

        if size not in word_dic:
            ans.append(0)
            continue

        if query.endswith("?"):
            a = query.replace('?', 'a')
            b = query.replace('?', 'z')
            ans.append(range_of(word_dic[size]['l'], a, b))
        else:
            a = query[::-1].replace('?', 'a')
            b = query[::-1].replace('?', 'z')
            ans.append(range_of(word_dic[size]['r'], a, b))

    return ans
