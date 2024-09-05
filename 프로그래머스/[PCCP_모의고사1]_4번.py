import heapq

h
def solution(program):
    answer = [0 for _ in range(11)]

    # 호출시간 + 실행시간 사이에 프로그램을 뽑아내고 점수 시간 순으로 나열한다.
    # 실행 종료 시간(이전 시작시간  + 이전 실행 시간) - 현재 호출 시간이 대기 시간이다.
    heap = []
    for score, call_time, work_time in program:
        heapq.heappush(heap, (call_time, [score, call_time, work_time]))

    start_time = 0
    priority, p = heapq.heappop(heap)
    end_time = p[1] + p[2]
    answer[0] = end_time
    while heap:
        wait_heap = []
        while heap and heap[0][0] <= end_time:
            # heap[0][0] = 다음 최소 실행시간을 의미한다.
            call_time, p = heapq.heappop(heap)
            # wait_heap에 점수 순으로 넣는다.
            score, call_time, work_time = p
            heapq.heappush(wait_heap, (score, [score, call_time, work_time]))
        # 여기 중 제일 점수 낮은 걸 사용한다.
        priorty, p = heapq.heappop(wait_heap)
        # 실행 종료 시간(이전 시작시간  + 이전 실행 시간) - 현재 호출 시간이 대기 시간이다.
        score, call_time, work_time = p
        answer[score] += end_time - call_time
        end_time += work_time
        answer[0] = end_time

        # wait_heap에 있던 값을 다시 heap에 넣는다.
        while wait_heap:
            score, p = heapq.heappop(wait_heap)
            score, call_time, work_time = p
            heapq.heappush(heap, (call_time, [score, call_time, work_time]))
        print(heap)

    return answer
