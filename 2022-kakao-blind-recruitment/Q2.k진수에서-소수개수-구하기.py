def to_k_notation(n, k):
    ans = []

    while n > 0:
        ans.append(str(n % k))
        n = n // k

    return ''.join(ans[::-1])


def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def solution(n, k):
    num_list = to_k_notation(n, k).split("0")
    return sum([1 for num in num_list if num and is_prime(int(num))])
