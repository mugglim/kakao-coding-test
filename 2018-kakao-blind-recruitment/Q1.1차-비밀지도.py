def to_binary(n, pad):
    b = bin(n)[2:]
    return "0" * (pad-len(b)) + b


def to_sharp(binary_text):
    return ''.join(map(lambda x: '#' if x == '1' else ' ', binary_text))


def solution(n, arr1, arr2):
    ans = []

    for a, b in zip(arr1, arr2):
        a_or_b = to_binary(a | b, n)
        ans.append(to_sharp(a_or_b))

    return ans
