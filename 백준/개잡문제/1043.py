import sys
from collections import defaultdict, deque

n, m = map(int, sys.stdin.readline().rstrip().split())

true_list = list(map(int, sys.stdin.readline().rstrip().split()))

if len(true_list) == 0:
    true_list = []
else:
    true_list = true_list[1:]

q = deque(true_list)

party = []
# 진실 거짓을 말할 수 있는 딕셔너리 정리
party_dict = dict()
participate_dict = defaultdict(list)

visited = [0 for _ in range(n + 1)]

for i in range(m):
    party.append(list(map(int, sys.stdin.readline().rstrip().split()))[1:])
    party_dict[i] = False

# 각 사람이 참여하는 파티 딕셔너리에 정리
for idx, pa in enumerate(party):
    for p in pa:
        participate_dict[p].append(idx)

while q:
    true_person = q.popleft()
    if visited[true_person] == 0:
        visited[true_person] = 1
        for party_idx in participate_dict[true_person]:
            party_dict[party_idx] = True
            # 해당 파티 IDX에 있는 사람들을 넣는다.
            for person in party[party_idx]:
                q.append(person)

answer = 0

for value in party_dict.values():
    if not value:
        answer += 1

print(answer)
