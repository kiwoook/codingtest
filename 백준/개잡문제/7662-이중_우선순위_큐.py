import heapq
import sys
from collections import defaultdict

INF = int(1e12)

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    k = int(sys.stdin.readline().rstrip())
    max_q = []
    min_q = []
    num_dict = defaultdict(int)
    max_answer = -INF
    min_answer = INF

    for _ in range(k):
        cmd, value = sys.stdin.readline().rstrip().split()
        value = int(value)
        if cmd == 'I':
            num_dict[value] += 1
            heapq.heappush(max_q, (-value, value))
            heapq.heappush(min_q, (value, value))
        if cmd == 'D':
            if value == 1 and len(max_q) > 0:
                p, v = heapq.heappop(max_q)
                while max_q and num_dict[v] <= 0:
                    p, v = heapq.heappop(max_q)
                if num_dict[v] > 0:
                    num_dict[v] -= 1
            if value == -1 and len(min_q) > 0:
                p, v = heapq.heappop(min_q)
                while min_q and num_dict[v] <= 0:
                    p, v = heapq.heappop(min_q)
                if num_dict[v] > 0:
                    num_dict[v] -= 1
    sw = 0
    for key, value in num_dict.items():
        if value >= 1:
            min_answer = min(key, min_answer)
            max_answer = max(key, max_answer)
            sw = 1

    if sw == 0:
        print("EMPTY")
    else:
        print(max_answer, min_answer)
