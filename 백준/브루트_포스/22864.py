a, b, c, m = map(int, input().split())

tired = 0
answer = 0
for hour in range(24):
    if tired + a > m:
        tired = tired - c if tired - c >= 0 else 0
        continue

    tired += a
    answer += b

print(answer)
