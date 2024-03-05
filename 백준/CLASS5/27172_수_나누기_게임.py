import sys

max_value = 1000001
visited = [0 for _ in range(max_value)]

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
scores = [0 for _ in range(max_value)]

for a in arr:
    visited[a] += 1

for i in range(0, n):
    for j in range(arr[i] * 2, max_value, arr[i]):
        if visited[j] == 1:
            scores[arr[i]] += 1
            scores[j] -= 1

answer = []
for i in range(0, n):
    answer.append(scores[arr[i]])

print(*answer)
