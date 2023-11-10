from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    sec = 0
    bridge = deque([0 for _ in range(bridge_length)])
    bridge_weight = 0
    while bridge_weight != 0 or len(truck_weights) != 0:
        bridge_weight -= bridge.popleft()
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                bridge_weight += truck
            else:
                bridge.append(0)
        sec += 1

    return sec


print(solution(2, 10, [7, 4, 5, 6]))
