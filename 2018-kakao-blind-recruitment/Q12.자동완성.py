class Trie:
    def __init__(self):
        self.head = {}

    def add(self, word):
        curr = self.head
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]

            if 'child' not in curr:
                curr['child'] = 1
            else:
                curr['child'] += 1

    def query(self, word):
        curr = self.head
        cnt = 0

        for ch in word:
            curr = curr[ch]
            cnt += 1

            if curr['child'] == 1:
                break

        return cnt


def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.add(word)

    for word in words:
        answer += trie.query(word)

    return answer
