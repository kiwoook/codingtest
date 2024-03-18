import sys

sys.setrecursionlimit(10000)


class Tree:
    def __init__(self, value=None, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left

def dfs_create(current_tree, value):
    if current_tree.value is None:
        current_tree.value = value
        return
    else:
        if current_tree.value < value:
            if current_tree.right is not None:
                dfs_create(current_tree.right, value)
            else:
                right_tree = Tree()
                current_tree.right = right_tree
                dfs_create(right_tree, value)
        else:
            if current_tree.left is not None:
                dfs_create(current_tree.left, value)
            else:
                left_tree = Tree()
                current_tree.left = left_tree
                dfs_create(left_tree, value)


def dfs_print(current_tree):
    if current_tree.value is None:
        return

    if current_tree.left is not None:
        dfs_print(current_tree.left)
    if current_tree.right is not None:
        dfs_print(current_tree.right)
    print(current_tree.value)


try:
    head = Tree()
    while True:
        user_input = int(sys.stdin.readline().rstrip())

        dfs_create(head, user_input)

except:
    dfs_print(head)
