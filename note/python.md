# Python-note

### re module

- re.match vs re.search
  - `re.match` searchs only from the **beginning of** the string
- re.findall
  - `re.findall` returns all non-overlapping matches of pattern in string, as a **list of strings or tuples**.

### FP in python

```python
from functools import reduce

# go
def go(*functions):
    return reduce(lambda x, f: f(x), functions)
```

### Iterator

```python
# get iterator object
iterator = iter(iterable)

# loop using next method
next(iterator)
next(iterator)
# ...
next(iterator) # Error iterator value is emtpy

```

### Time

- 시각 [s1,e1] 는 [s2, e2]의 구간에 포함된다.
  1. s1 <= e2
  2. e1 >= s2

```python
# 'hh:mm:ss' => second
def second_of(date):
    h,m,s = map(int,date.split(':'))
    return h * 3600 + m * 60 + s

# second => 'hh:mm:ss"
def format_of(second):
    ans = []
    quotient_list = [3600, 60, 1]

    for quotient in quotient_list:
        ans.append(str(second // quotient))
        second %= quotient

    return ':'.join(ans)

```

### Prime number

```python
def is_prime(n):
  for i in range(2, int(n ** 0.5) + 1):
      if x % i == 0:
          return False
  return True

```

### Detect cycle in directed graph

```python
from collections import deque

# using DFS
def has_cycle_dfs(graph):
    # -1 : unvisited vertex
    # 0 : visiting vertex
    # 1 : visited vertex

    visited = {node: -1 for node in graph}

    def dfs(node):
        visited[node] = 0
        for adj_node in graph:
            if visited[adj_node] == 1: continue
            if visited[adj_node] == 0: return True
            if dfs(adj_node): return True

        visited[node] = 1
        return False

    for node in visited:
        if visited[node] == -1:
            if dfs(node1): return True

    return False


# using topology sort
def has_cycle_topology_sort(graph):
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

    # 위상 정렬 후, 모든 노드의 진입 차수는 0이 되어야 함
    return not sum(indegree_list) == 0
```

### Ref.

- [geeksforgeeks](https://www.geeksforgeeks.org/python-re-search-vs-re-match/)
- [python-docs](https://docs.python.org/)
