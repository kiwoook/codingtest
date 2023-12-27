import heapq
import sys

n = int(input())

heap = []

input_list = []
for i in range(n):
    input_list.append(int(sys.stdin.readline().strip()))

for num in input_list:
    if num == 0:
        if len(heap) == 0:
            print('0')
        else:
            idx, value = heapq.heappop(heap)
            print(value)
    else:
        heapq.heappush(heap, (abs(num), num))
