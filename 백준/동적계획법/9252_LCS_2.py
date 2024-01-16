word1 = " " + input()
word2 = " " + input()

LCS = [[0 for _ in range(len(word2))] for _ in range(len(word1))]
for idx1, w1 in enumerate(word1):
    for idx2, w2 in enumerate(word2):
        if idx1 == 0 or idx2 == 0:
            continue
        elif w1 == w2:
            LCS[idx1][idx2] = LCS[idx1 - 1][idx2 - 1] + 1
        else:
            LCS[idx1][idx2] = max(LCS[idx1 - 1][idx2], LCS[idx1][idx2 - 1])
print(LCS[len(word1) - 1][len(word2) - 1])

value = LCS[len(word1) - 1][len(word2) - 1]
answer = []

# 역추적
for i in range(len(word1) - 1, -1, -1):
    for k in range(len(word2) - 1, -1, -1):
        if LCS[i][k] - 1 == LCS[i - 1][k - 1] and word1[i] == word2[k] and LCS[i][k] == value:
            answer.append(word1[i])
            value -= 1
            break

answer.reverse()
print(''.join(answer))
