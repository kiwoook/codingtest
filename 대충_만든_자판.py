def solution(keymap, targets):
    answer = []
    word_set = set([])
    min_click_dict = {}

    for arr in keymap:
        for a in arr:
            word_set.add(a)

    for word in word_set:
        min_click = 101
        for i in range(len(keymap)):
            tmp = keymap[i].find(word)
            if tmp == -1:
                continue
            if tmp <= min_click:
                min_click = tmp
        min_click_dict[word] = min_click+1

    for target in targets:
        cnt = 0
        for t in target:
            if t in min_click_dict:
                cnt += min_click_dict[t]
            else:
                cnt = -1
                break
        answer.append(cnt)

    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
