import sys
from collections import defaultdict, deque
from itertools import combinations


def checking_bfs(visited):
    # visited가 0인 것을 기준으로 모두 연결되어있는지 확인
    q = deque([])
    check_visited = [v for v in visited]
    for i in range(1, n + 1):
        if not check_visited[i]:
            q.append(i)
            check_visited[i] = True
            break

    while q:
        nd = q.popleft()
        for nd1 in graph[nd]:
            if not check_visited[nd1]:
                check_visited[nd1] = True
                q.append(nd1)

    return all(check_visited[1:])


answer = int(1e12)
n = int(sys.stdin.readline().rstrip())
person_list = [0]
person_list.extend(list(map(int, sys.stdin.readline().rstrip().split())))

graph = defaultdict(list)

for node in range(1, n + 1):
    graph[node] = list(map(int, sys.stdin.readline().rstrip().split()))[1:]

for i in range(1, n // 2 + 1):
    comb = list(combinations(range(1, n + 1), i))

    for cmb in comb:
        vs1 = [False for _ in range(n + 1)]
        for cb in cmb:
            vs1[cb] = True
        vs2 = [not v for v in vs1]

        if checking_bfs(vs1) and checking_bfs(vs2):
            hap1 = 0
            hap2 = 0
            for i in range(1, n + 1):
                if vs1[i]:
                    hap1 += person_list[i]
                if not vs1[i]:
                    hap2 += person_list[i]
            answer = min(answer, abs(hap1 - hap2))

if answer == int(1e12):
    print(-1)
else:
    print(answer)
