from collections import deque


def solution(info, edges):
    n = len(info)
    ans = 1

    def can_visit(bit, idx): return not (bit & 1 << idx)
    def set_visit(bit, idx): return bit | 1 << idx

    adj = [[] for _ in range(n)]

    for [a, b] in edges:
        adj[a].append(b)

    queue = deque([(0, [1, 0], 0, adj[0][::])])

    while queue:
        node, cnt, bit, child_nodes = queue.popleft()

        for child_node in child_nodes:
            new_cnt = [*cnt]

            new_cnt[info[child_node]] += 1
            new_bit = set_visit(bit, child_node)
            new_child_node = [*child_nodes, *adj[child_node]]

            if new_cnt[0] == new_cnt[1]:
                continue

            if can_visit(bit, child_node):
                ans = max(ans, new_cnt[0])
                queue.append([child_node, new_cnt, new_bit, new_child_node])

    return ans
