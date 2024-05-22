import sys

sys.setrecursionlimit(10 ** 5)


class TreeNode:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None


def find_pre_order(in_start, in_end, post_start, post_end):
    global in_order_list, post_order_list

    if in_start > in_end or post_start > post_end:
        return None

    root_value = post_order_list[post_end]
    root = TreeNode(root_value)
    root_index = in_order_list.index(root_value)
    left_size = root_index - in_start

    root.left = find_pre_order(in_start, root_index - 1, post_start, post_start + left_size - 1)
    root.right = find_pre_order(root_index + 1, in_end, post_start + left_size, post_end - 1)

    return root


def pre_order(node):
    if node:
        print(node.value, end=" ")
        pre_order(node.left)
        pre_order(node.right)


n = int(input())

in_order_list = list(map(int, sys.stdin.readline().rstrip().split()))

post_order_list = list(map(int, sys.stdin.readline().rstrip().split()))

tree_root = find_pre_order(0, len(in_order_list) - 1, 0, len(post_order_list) - 1)

pre_order(tree_root)
