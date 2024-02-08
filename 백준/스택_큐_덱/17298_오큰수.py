n = int(input())
a = list(map(int, input().split()))

stack = []
result = [-1] * n  # 결과 배열을 -1로 초기화

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        result[stack.pop()] = a[i]

    stack.append(i)

print(*result)