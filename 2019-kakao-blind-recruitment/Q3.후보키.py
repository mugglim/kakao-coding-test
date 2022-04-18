from itertools import combinations


def solution(relation):
    col_size = len(relation[0])
    col_list = [i for i in range(col_size)]
    cnt = 0
    visited = {}

    def is_unique_key(key_list):
        val_list = {}

        for row in relation:
            val = ''.join([v for col_idx, v in enumerate(row)
                          if col_idx in key_list])
            if val in val_list:
                return False
            val_list[val] = True

        return True

    def is_min_key(key_list):
        set_a = set(key_list)

        for visited_key_list in visited.keys():
            set_b = set(visited_key_list)

            if set_b.issubset(set_a) and len(set_a - set_b) != len(set_a):
                return False

        return True

    for pick in range(1, col_size + 1):
        for key_list in combinations(col_list, pick):

            if is_unique_key(key_list) and is_min_key(key_list):
                visited[tuple(key_list)] = True

    print(visited)
    return len(visited)
