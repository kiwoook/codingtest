from collections import deque


def solution(A, B):
    answer = 0

    A.sort(reverse=True)
    B.sort(reverse=True)

    A, B = deque(A), deque(B)

    while B:
        # A랑 B를 비교
        if A[0] < B[0]:
            A.popleft()
            B.popleft()
            answer += 1
        else:
            A.popleft()
            B.pop()

    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
