from collections import Counter


def solution(picks, minerals):
    answer = 0
    minerals_list = []
    idx = 0

    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:sum(picks) * 5]

    for i in range(0, len(minerals), 5):
        minerals_list.append(minerals[i:i + 5])

    sorted_minerals = sorted(minerals_list,
                             key=lambda x: (Counter(x)["diamond"], Counter(x)["iron"], Counter(x)["stone"]),
                             reverse=True)

    for mineral_list in sorted_minerals:
        while picks[idx] == 0:
            idx += 1
        for m in mineral_list:
            if idx == 0:
                answer += 1
            if idx == 1:
                if m == "diamond":
                    answer += 5
                else:
                    answer += 1
            if idx == 2:
                if m == "diamond":
                    answer += 25
                elif m == "iron":
                    answer += 5
                else:
                    answer += 1
        picks[idx] -= 1

    return answer


print(solution([0, 0, 2],
               ["stone", "stone", "stone", "stone", "stone", "diamond", "diamond", "diamond", "diamond", "diamond",
                "diamond"]))
