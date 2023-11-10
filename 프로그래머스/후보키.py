from itertools import combinations

def solution(relation):
    n = len(relation)
    m = len(relation[0])
    unique_set = set()
    answer = 0

    for i in range(1, m + 1):
        for comb in combinations(range(m), i):
            # 현재 조합으로 유일성을 만족하는지 확인
            unique = set()
            is_unique = True
            for row in relation:
                key = tuple(row[c] for c in comb)

                if key in unique:
                    is_unique = False
                    break
                unique.add(key)

            if is_unique:
                # 최소성을 만족하는지 확인
                is_minimal = True
                for u in unique_set:
                    if set(u).issubset(set(comb)):
                        is_minimal = False
                        break
                if is_minimal:
                    unique_set.add(comb)
                    answer += 1
    return answer


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
