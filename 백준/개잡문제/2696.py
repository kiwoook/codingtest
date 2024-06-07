import heapq
import math
import sys


def find_median(max_heap):
    return max_heap[0][1]


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    m = int(sys.stdin.readline().rstrip())
    number_list = []
    for _ in range(math.ceil(m / 10)):
        number_list.append(list(map(int, sys.stdin.readline().rstrip().split())))
    number_list = sum(number_list, [])
    max_q = []
    min_q = []
    answer_list = []
    for idx, number in enumerate(number_list):
        if len(max_q) == len(min_q):
            heapq.heappush(max_q, (-number, number))
        else:
            heapq.heappush(min_q, number)

        if min_q and max_q[0][1] > min_q[0]:
            p, max_v = heapq.heappop(max_q)
            min_v = heapq.heappop(min_q)
            heapq.heappush(min_q, max_v)
            heapq.heappush(max_q, (-min_v, min_v))

        if idx % 2 == 0:
            answer_list.append(find_median(max_q))

    print(len(answer_list))

    # 배열 크기와 상관없이 10개씩 자르기
    answer_list = [answer_list[idx:idx + 10] for idx in range(0, len(answer_list), 10)]

    for answer in answer_list:
        print(*answer)
