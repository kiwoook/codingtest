
import heapq
import sys


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    answer = 0
    n = int(sys.stdin.readline().rstrip())
    file_list = list(map(int, sys.stdin.readline().rstrip().split()))
    heapq.heapify(file_list)
    while len(file_list) != 1:
        hap = 0
        for i in range(2):
            hap += heapq.heappop(file_list)
        heapq.heappush(file_list, hap)

        answer += hap

    print(answer)

