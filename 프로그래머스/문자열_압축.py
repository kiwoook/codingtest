def solution(s):
    len_s = len(s)
    answer = len_s
    for i in range(1, len(s) // 2):
        chunk_list = [s[k:k + i] for k in range(0, len_s, i)]
        compress_s, pointer = '', chunk_list[0]
        cnt = 1
        for idx, value in enumerate(chunk_list[1:]):
            if value == pointer:
                cnt += 1
            else:
                compress_s += str(cnt)+pointer if cnt > 1 else pointer
                pointer = value
                cnt = 1
        compress_s += str(cnt) + pointer if cnt > 1 else pointer

        answer = min(answer, len(compress_s))

    return answer


print(solution("abcabcdede"))
