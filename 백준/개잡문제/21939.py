import heapq
import sys
from collections import defaultdict

hard_heap = []
easy_heap = []
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    number, level = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(hard_heap, (-level, -number))
    heapq.heappush(easy_heap, (level, number))

m = int(sys.stdin.readline().rstrip())

solved_dict = defaultdict(int)

for _ in range(m):
    cmd_list = list(sys.stdin.readline().rstrip().split())

    if cmd_list[0] == 'add':
        number = int(cmd_list[1])
        heapq.heappush(hard_heap, (-int(cmd_list[2]), -int(cmd_list[1])))
        heapq.heappush(easy_heap, (int(cmd_list[2]), int(cmd_list[1])))
    if cmd_list[0] == 'solved':
        target = int(cmd_list[1])
        # 실제로 제거하면 오래 걸림, 메모리가 넉넉하니 dict 사용
        solved_dict[target] += 1
    if cmd_list[0] == 'recommend':
        if cmd_list[1] == '1':
            while solved_dict[abs(hard_heap[0][1])] != 0:
                solved_dict[abs(hard_heap[0][1])] -= 1
                heapq.heappop(hard_heap)

            print(abs(hard_heap[0][1]))

        elif cmd_list[1] == '-1':
            while solved_dict[easy_heap[0][1]] != 0:
                solved_dict[easy_heap[0][1]] -= 1
                heapq.heappop(easy_heap)

            print(easy_heap[0][1])
