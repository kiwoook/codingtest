def remain_tree(value, target):
    cnt = 0
    for tree in tree_list:
        if tree > value:
            cnt += tree - value

    if cnt == target:
        return 0
    elif cnt < target:
        return 1
    else:
        return -1


n, m = map(int, input().split())

tree_list = list(map(int, input().split()))

left, right = 0, max(tree_list)

result = 0

while left <= right:
    mid = (left + right) // 2
    v = remain_tree(mid, m)

    if v == -1 or v == 0:
        left = mid + 1
        result = mid
    if v == 1:
        right = mid - 1

print(result)
