def solution(gems):
    gem_set = set(gems)
    gem_window = {}
    ans = []

    r = 0
    n = len(gems)
    gen_kind_count = len(gem_set)

    for l in range(n):
        while r < n and len(gem_window) < gen_kind_count:
            r_gem = gems[r]
            if r_gem not in gem_window:
                gem_window[r_gem] = 0
            gem_window[r_gem] += 1

            r += 1

        if r <= n and len(gem_window) == gen_kind_count:
            dist = r - (l+1)

            if not ans or dist < (ans[1] - ans[0]):
                ans = [l+1, r]

        l_gem = gems[l]
        if l_gem in gem_window:
            if gem_window[l_gem] == 1:
                del gem_window[l_gem]
            else:
                gem_window[l_gem] -= 1

    return ans
