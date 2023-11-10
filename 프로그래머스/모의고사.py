def solution(answers):
    answer = []
    len_answer = len(answers)
    a = [0] * len_answer
    c = [0] * len_answer
    b = [0] * len_answer

    a1 = [1, 2, 3, 4, 5]
    b1 = [1, 3, 4, 5]
    c1 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]

    a_idx = 0
    b_idx = 0
    c_idx = 0

    for i in range(len_answer):
        a[i] = a1[a_idx]
        a_idx += 1
        if a_idx == 5:
            a_idx = 0
        if i % 2 == 0:
            b[i] = 2
        else:
            b[i] = b1[b_idx]
            b_idx += 1
        if b_idx == 4:
            b_idx = 0
        c[i] = c1[c_idx]
        c_idx += 1
        if c_idx == 10:
            c_idx = 0

    print(a,b,c)

    for i in range(len_answer):
        if a[i] == answers[i]:
            cnt[0] += 1
        if b[i] == answers[i]:
            cnt[1] += 1
        if c[i] == answers[i]:
            cnt[2] += 1

    print(cnt)
    for i in range(3):
        if cnt[i] == max(cnt):
            answer.append(i + 1)

    return answer

#
# print(solution([[1,3,2,4,2]]))
print(solution([2, 3, 4, 5, 1]))
