def solution(s):
    answer = 0
    list_s = list(s)
    len_s = len(list_s)
    compare_idx = 0
    while compare_idx < len_s:
        same_cnt = 0
        diff_cnt = 0
        for i in range(compare_idx, len_s):
            if list_s[compare_idx] == list_s[i]:
                same_cnt += 1
            else:
                diff_cnt += 1
            if same_cnt == diff_cnt or i == len_s - 1:
                compare_idx = i + 1
                answer += 1
                break

    return answer


print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
