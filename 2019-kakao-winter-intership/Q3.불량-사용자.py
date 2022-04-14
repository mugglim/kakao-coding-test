# TODO : 변수명 리팩토링 및 함수 분리

class Trie:
    def __init__(self):
        self.head = {}

    def add(self, user_id):
        curr = self.head

        for ch in user_id:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]

        curr['leaf'] = True

    def search(self, ban_id):
        find_id_list = []
        n = len(ban_id)

        def backtrack(curr, find_id):
            if len(find_id) == n:
                if "leaf" in curr:
                    find_id_list.append(find_id)
                return

            b_ch = ban_id[len(find_id)]

            for ch in curr:
                if ch in ['leaf']:
                    continue
                if b_ch == "*" or b_ch == ch:
                    backtrack(curr[ch], find_id + ch)

        backtrack(self.head, "")
        return find_id_list


def count_all_case(find_id_list):
    visited_set_list = []
    visited_id = set()

    n = len(find_id_list)
    cnt = 0

    def backtrack(idx, id_set):
        nonlocal cnt

        if idx == n:
            cnt += 1
            return

        for find_id in find_id_list[idx]:
            new_id_set = set([*id_set, find_id])

            if new_id_set not in visited_set_list and find_id not in visited_id:
                visited_set_list.append(new_id_set)

                visited_id.add(find_id)
                backtrack(idx + 1, new_id_set)
                visited_id.remove(find_id)

    backtrack(0, set())
    return cnt


def solution(user_id, banned_id):
    trie = Trie()
    find_id_list = []

    for u_id in user_id:
        trie.add(u_id)

    for b_id in banned_id:
        find_id_list.append(trie.search(b_id))

    return count_all_case(find_id_list)


print(solution(["12345", "12453", "aaaaa"], ['*****', '*****']))
