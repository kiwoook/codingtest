def solution(max_cap, n, deliveries, pickups):
    answer = 0

    # 맨 뒤에 0을 소거하자.
    while deliveries and deliveries[-1] == 0:
        deliveries.pop()

    while pickups and pickups[-1] == 0:
        pickups.pop()

    while deliveries or pickups:
        # 결국 최대 길이로 가야한다.
        length = max(len(deliveries), len(pickups))

        cap = max_cap
        while deliveries and cap != 0:
            if deliveries[-1] > cap:
                deliveries[-1] -= cap
                cap = 0
            else:
                cap -= deliveries[-1]
                deliveries.pop()

        while deliveries and deliveries[-1] == 0:
            deliveries.pop()

        cap = max_cap
        while pickups and cap != 0:
            if pickups[-1] > cap:
                pickups[-1] -= cap
                cap = 0
            else:
                cap -= pickups[-1]
                pickups.pop()

        while pickups and pickups[-1] == 0:
            pickups.pop()

        answer += length * 2

    return answer


print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
