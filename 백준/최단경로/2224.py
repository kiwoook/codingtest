import sys

INF = int(1e9)
n = int(sys.stdin.readline().rstrip())

distance = [[INF for _ in range(123)] for _ in range(123)]

answer_set = set()

for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split(' => ')
    distance[ord(a)][ord(b)] = 0

for middle in range(ord('A'), ord('z') + 1):
    for start in range(ord('A'), ord('z') + 1):
        for end in range(ord('A'), ord('z') + 1):
            if distance[start][end] > distance[start][middle] + distance[middle][end]:
                distance[start][end] = distance[start][middle] + distance[middle][end]

answer_list = []

for start in range(ord('A'), ord('z') + 1):
    for end in range(ord('A'), ord('z') + 1):
        if start != end and distance[start][end] == 0:
            answer_list.append((start, end))

answer_list.sort(key=lambda x: (x[0], x[1]))

print(len(answer_list))
for start, end in answer_list:
    print(f"{chr(start)} => {chr(end)}")
