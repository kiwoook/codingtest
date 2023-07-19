from collections import Counter

def solution(citations):
    citations.sort()
    cnt_cita = Counter(citations)
    print(cnt_cita)
    set_cita = set(citations)
    med = int(len(citations) / 2) + 1
    for i in range(citations[med], citations[0]-1, -1):
        print(i)
        cnt = 0
        for cite in set_cita:
            if cite >= i:
                cnt += cnt_cita[cite]

            if cnt >= i:
                return i

    return len(citations)

# count 메소드는 시간적 복잡도가 크다.
# Counter를 사용하자.

print(solution([19, 16, 2, 2, 2]))
