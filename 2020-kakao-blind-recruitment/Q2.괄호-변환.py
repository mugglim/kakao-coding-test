from collections import Counter


def is_right(s):
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack or stack[-1] != "(":
                return False
            stack.pop()

    return len(stack) == 0


def split_uv(s):
    counter = {'(': 0, ')': 0}
    res = ['', '']

    for i, ch in enumerate(s):
        counter[ch] += 1

        if counter['('] == counter[')']:
            res = [s[:i+1], s[i+1:]]
            break

    return res


def trans(s):
    dic = {'(': ')', ')': '('}
    return ''.join([dic[ch] for ch in s])


def solution(p):
    if not p:
        return ''
    if is_right(p):
        return p

    u, v = split_uv(p)

    if is_right(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + trans(u[1:-1])
