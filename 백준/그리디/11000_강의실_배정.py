import sys
import heapq


study_list = []

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    study_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

study_list.sort(key=lambda x: (x[0], x[1]))

# 힙큐를 사용해서 순위를 조정하면서 채우면 될듯?....
heap = [study_list[0][1]]


for start_time, end_time in study_list[1:]:
    if heap[0] <= start_time:
        heapq.heappop(heap)
    heapq.heappush(heap, end_time)

print(len(heap))