from itertools import combinations

n, k = map(int, input().split())

using = ['a', 'n', 't', 'i', 'c']
max_cnt = 0
word_list = []
if k < 5:
    print(0)
else:
    k = k - 5
    cnt = [0] * 27

    for _ in range(n):
        # 사용하는 단어들을 분석
        answer = 0
        s = input()
        word_list.append(s)
        for x in s:
            cnt[ord(x) - ord('a')] = 1

    # using을 제외하고 나머지를 추출한다.
    for u in using:
        cnt[ord(u) - ord('a')] = 0

    checking_list = []

    for i in range(27):
        if cnt[i] == 1:
            checking_list.append(chr(i + ord('a')))

    # k 개수 만큼 선택하자.
    able_list = []
    if len(checking_list) < k:
        print(n)
        exit(0)
    else:
        able_list = list(combinations(checking_list, k))

    for able in able_list:
        tmp_using = using[:]
        cnt = 0

        for a in able:
            tmp_using.append(a)
        # word_list에서 가능한 것인지 분석한다.

        for word in word_list:
            sw = 1
            for w in word:
                if w not in tmp_using:
                    sw = 0
                    break
            if sw == 1:
                cnt += 1

        if max_cnt < cnt:
            max_cnt = cnt

    print(max_cnt)


