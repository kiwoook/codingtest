T = int(input())

for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    print(min(a), max(a))
