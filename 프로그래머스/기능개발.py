from collections import deque
def solution(progresses, speeds):
    answer = []
    complete = len(progresses) * 100
    complete_list = [0] * len(progresses)
    cnt = 0
    while any(speeds):
        # 더하기
        cnt += 1
        progresses = [x + y for x, y in zip(progresses, speeds)]
        # 100인지 체크
        for idx, progress in enumerate(progresses):
            if progress >= 100:
                complete_list[idx] = cnt
                progresses[idx] = -1
                speeds[idx] = 0

    complete_deque = deque(complete_list)

    while complete_deque:
        idx = 0

        while complete_deque[idx] <= complete_deque[0]:
            if idx == len(complete_deque)-1:
                idx += 1
                break
            idx += 1

        answer.append(idx)
        for _ in range(idx):
            complete_deque.popleft()

    return answer


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
