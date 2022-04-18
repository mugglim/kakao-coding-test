import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, x, val):
        self.x = x
        self.val = val
        self.left = None
        self.right = None


def pre_order(node, val):
    def backtrack(curr):
        if not curr:
            return

        res.append(curr.val)

        backtrack(curr.left)
        backtrack(curr.right)

    backtrack(node)
    return res


def post_order(node):
    res = []

    def backtrack(curr):
        if not curr:
            return

        backtrack(curr.left)
        backtrack(curr.right)

        res.append(curr.val)

    backtrack(node)
    return res


def solution(nodeinfo):
    node_list = [[x, y, i+1] for i, [x, y] in enumerate(nodeinfo)]
    node_list.sort(key=lambda x: (-x[1], x[0]))  # sort by y,x asc

    max_level = node_list[0][1]
    node_list = list(map(lambda x: [x[0], max_level-x[1], x[2]], node_list))

    root_node_x, _, root_node_val = node_list[0]
    root_node = Node(root_node_x, root_node_val)

    node_info_dic = {
        0: [root_node]
    }

    for [x, level, val] in node_list[1:]:
        if level not in node_info_dic:
            node_info_dic[level] = []
        node_info_dic[level].append(Node(x, val))

    levels = list(node_info_dic.keys())[1:]

    for level in levels:
        for child_node in node_info_dic[level]:
            curr = root_node
            while True:
                if child_node.x < curr.x:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = child_node
                        break
                elif child_node.x > curr.x:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = child_node
                        break

    return [pre_order(root_node), post_order(root_node)]
