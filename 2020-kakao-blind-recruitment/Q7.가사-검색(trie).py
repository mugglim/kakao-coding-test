import sys
sys.setrecursionlimit(10**6)


class Trie:
    def __init__(self):
        self.head = {'leaf_cnt': 0}

    def add(self, word):

        def backtrack(i, curr):
            if i == len(word):
                return 1

            ch = word[i]

            if ch not in curr:
                curr[ch] = {'leaf_cnt': 0}

            backtrack(i+1, curr[ch])
            curr[ch]['leaf_cnt'] += 1

        backtrack(0, self.head)
        self.head['leaf_cnt'] += 1

    def query(self, word):
        curr = self.head

        for i in range(len(word) - 1):
            ch = word[i]
            next_ch = word[i+1]

            # for like "????"
            if ch == "?":
                return curr['leaf_cnt']

            if ch not in curr:
                return 0
            if next_ch == "?":
                return curr[ch]['leaf_cnt']
            curr = curr[ch]

        return 0


def solution(words, queries):
    trie_dic = {}
    r_trie_dic = {}
    ans = []

    for word in words:
        n = len(word)

        if n not in trie_dic:
            trie_dic[n] = Trie()
            r_trie_dic[n] = Trie()

        trie_dic[n].add(word)
        r_trie_dic[n].add(word[::-1])

    for query_word in queries:
        n = len(query_word)

        if n not in trie_dic:
            ans.append(0)
            continue

        if query_word.endswith("?"):
            ans.append(trie_dic[n].query(query_word))
        else:
            ans.append(r_trie_dic[n].query(query_word[::-1]))

    return ans
