def solution_failed(board, skills):
    n, m = len(board), len(board[0])
    answer = n * m

    # 시간 복잡도 O(n * m * s) 이므로 시간 초과가 발생할 수 밖에 없음.

    for skill in skills:
        t, r1, c1, r2, c2, degree = skill
        if t == 1:
            for i in range(r1, r2 + 1):
                for k in range(c1, c2 + 1):
                    sw = 0
                    if board[i][k] <= 0:
                        sw = 1
                    board[i][k] -= degree
                    if sw == 0 and board[i][k] <= 0:
                        answer -= 1
        else:
            for i in range(r1, r2 + 1):
                for k in range(c1, c2 + 1):
                    sw = 0
                    if board[i][k] > 0:
                        sw = 1
                    board[i][k] += degree
                    if sw == 0 and board[i][k] > 0:
                        answer += 1

    return answer


def solution(board, skills):
    n, m = len(board), len(board[0])
    answer = 0
    hap = [[0 for _ in range(m)] for _ in range(n)]

    for skill in skills:
        t, r1, c1, r2, c2, degree = skill

        if t == 1:
            degree = -degree
        # 배열 선 초기화
        hap[r1][c1] += degree
        if r2 + 1 < n:
            hap[r2 + 1][c1] += -degree
        if c2 + 1 < m:
            hap[r1][c2 + 1] += -degree
        if r2 + 1 < n and c2 + 1 < m:
            hap[r2 + 1][c2 + 1] += degree

    # 누적합 연산 시행 오른쪽으로
    for i in range(0, n):
        for k in range(1, m):
            hap[i][k] += hap[i][k - 1]

    # 누적합 연산 위에서 아래로
    for i in range(1, n):
        for k in range(0, m):
            hap[i][k] += hap[i - 1][k]

    # board + hap 배열 합치기
    for i in range(0, n):
        for k in range(0, m):
            board[i][k] += hap[i][k]
            if board[i][k] > 0:
                answer += 1

    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
