import heapq

def solution_failed(scoville, K):
    answer = 0
    scoville.sort()

    while scoville[0] < K:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        scoville.sort()
        first = scoville.pop(0)
        second = scoville.pop(0)
        scoville.insert(0, first + second * 2)
        answer += 1
    return answer

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2:
        min_v = heapq.heappop(scoville)

        if min_v >= K:
            return answer
        else:
            min2_v = heapq.heappop(scoville)
            heapq.heappush(scoville, min_v + min2_v*2)
            answer += 1
    if heapq.heappop(scoville) >= K:
        return answer
    else:
        return -1



print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([2,3], 5))
print(solution([4],5))