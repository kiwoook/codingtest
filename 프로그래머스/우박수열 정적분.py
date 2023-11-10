def solution(k, ranges):
    answer = []
    graph_value = []

    while k != 1:
        graph_value.append(k)
        if k % 2 == 0:
            k /= 2
        else:
            k = k * 3 + 1

    # 1값도 넣어줘야함
    graph_value.append(k)

    integral_list = []
    for i in range(0, len(graph_value) - 1):
        integral_list.append((graph_value[i] + graph_value[i + 1]) / 2)

    for ran in ranges:
        start, end = ran
        end = len(graph_value) + end - 1
        if start == end:
            answer.append(0)
        elif start > end:
            answer.append(-1)
        else:
            # 여기서 n^2이 나온다. DP로 해결해야할거 같은 부분?
            answer.append(sum(integral_list[start:end]))

    return answer


print(solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]]))
