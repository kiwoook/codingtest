import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

# 할아버지 노드가 같고 부모가 달라야함....


while n != 0 and k != 0:
    num_list = list(map(int, sys.stdin.readline().rstrip().split()))
    sequence_list = [[num_list[0]]]
    answer = 0

    parent = [0 for _ in range(1000001)]
    parent[0] = -1

    idx = 1
    while idx < len(num_list):
        tmp = [num_list[idx]]
        while idx + 1 < len(num_list) and num_list[idx] + 1 == num_list[idx + 1]:
            idx += 1
            tmp.append(num_list[idx])
        sequence_list.append(tmp)
        idx += 1

    idx = 1
    parent_idx = 0

    while idx < len(sequence_list):
        for v in sequence_list[idx]:
            parent[v] = num_list[parent_idx]

        idx += 1
        parent_idx += 1

    for v in num_list:
        if parent[k] != parent[v] and parent[parent[k]] == parent[parent[v]]:
            answer += 1

    print(answer)

    n, k = map(int, sys.stdin.readline().rstrip().split())
