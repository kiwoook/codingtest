correct = [1, 1, 2, 2, 2, 8]
b = [c - a for c, a in zip(correct, list(map(int, input().split())))]
print(*b)
