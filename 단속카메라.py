from itertools import combinations


def solution_failed(routes):
    list_set = list()
    len_routes = len(routes)
    for idx_1, route_1 in enumerate(routes):
        for idx_2, route_2 in enumerate(routes):
            if idx_1 != idx_2 and idx_1 < idx_2:
                if route_1[1] >= route_2[0]:
                    list_set.append({idx_1, idx_2})
    for i in range(1, len_routes + 1):
        comb_list = (list(combinations(list_set, i)))
        hap_list = []
        for comb in comb_list:
            hap_set = set([])
            for c in comb:
                hap_set.update(c)
            hap_list.append(hap_set)

        for hap in hap_list:
            if len(hap) == len_routes:
                return i

    return len_routes + 1


def solution(routes):
    answer = 0

    routes.sort(key=lambda x: x[1])

    camera_pos = -30001

    for route in routes:
        if route[0] <= camera_pos:
            continue
        else:
            answer += 1
            camera_pos = route[1]

    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
