n, x = map(int, input().split())

visit_list = list(map(int, input().split()))
cnt = 1

start = 0
end = start + x

max_visit = 0
total = sum(visit_list[start:end])
max_visit = max(max_visit, total)

for i in range(n - x):
    total = total - visit_list[i] + visit_list[i + x]
    if max_visit < total:
        cnt = 1
        max_visit = total
    elif max_visit == total:
        cnt += 1

if max_visit != 0:
    print(max_visit)
    print(cnt)
else:
    print("SAD")
