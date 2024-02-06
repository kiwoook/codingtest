a = list(map(int, input().split()))
print(sum([value * value for value in a]) % 10)
