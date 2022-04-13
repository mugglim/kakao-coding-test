from collections import deque


def has_cycle(graph):
    n = len(graph)
    indegree_list = [0] * n
    for adj_node_list in graph:
        for adj_node in adj_node_list:
            indegree_list[adj_node] += 1

    queue = deque([node for node in range(n) if indegree_list[node] == 0])

    while queue:
        node = queue.popleft()
        for adj_node in graph[node]:
            indegree_list[adj_node] -= 1
            if indegree_list[adj_node] == 0:
                queue.append(adj_node)

    return not sum(indegree_list) == 0


def solution(n, path, order):
    ud_graph = [[] for _ in range(n)]
    d_graph = [[] for _ in range(n)]
    visited_set = set()

    for [a, b] in path:
        ud_graph[a].append(b)
        ud_graph[b].append(a)

    queue = deque([0])
    visited_set.add(0)

    while queue:
        node = queue.popleft()
        for child_node in ud_graph[node]:
            if child_node not in visited_set:
                visited_set.add(child_node)
                queue.append(child_node)
                d_graph[child_node].append(node)

    for [a, b] in order:
        d_graph[b].append(a)

    return not has_cycle(d_graph)
