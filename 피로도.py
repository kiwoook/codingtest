from itertools import permutations

def solution(k, dungeons):
    max_cnt = 0
    perm_dungeons = list(permutations(dungeons))
    for dungeon in perm_dungeons:
        hp = k
        cnt = 0
        dungeon = list(dungeon)
        for d in dungeon:
            if hp >= d[0]:
                hp -= d[1]
                cnt += 1
            else:
                break
        if cnt > max_cnt:
            max_cnt = cnt
        if max_cnt == len(dungeon):
            break
    return max_cnt


