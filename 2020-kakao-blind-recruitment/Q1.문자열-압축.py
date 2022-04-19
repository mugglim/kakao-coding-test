def parse(s, window_size):
    n = len(s)
    res = []
    word_info = [1, s[:window_size]]
    l = window_size
    
    def add_word():
        word = str(word_info[0]) + word_info[1] if word_info[0] > 1 else word_info[1]
        res.append(word)        
    

    while l < n:
        new_word = s[l:l+window_size]

        if word_info[1] == new_word:
            word_info[0] += 1
        else:
            add_word();
            word_info = [1, s[l:l+window_size]]

        l += window_size

    
    # remain word
    add_word();
    
    return len(''.join(res))


def solution(s):
    ans = len(s)

    for window_size in range(1, len(s) // 2 + 1):
        ans = min(ans, parse(s, window_size))

    return ans

