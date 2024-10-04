import sys


def postorder(preorder, inorder):
    if len(preorder) == 0:
        return []
    if len(preorder) == 1:
        return [preorder[0]]

    # 루트 찾기
    root = preorder[0]
    root_idx = inorder.index(root)

    left = postorder(preorder[1:1 + root_idx], inorder[:root_idx])
    right = postorder(preorder[1 + root_idx:], inorder[root_idx + 1:])

    return left + right + [root]


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    preorder_list = sys.stdin.readline().rstrip().split()
    inorder_list = sys.stdin.readline().rstrip().split()

    print(*postorder(preorder_list, inorder_list))
