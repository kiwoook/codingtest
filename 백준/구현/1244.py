import sys


def change_swtich(idx):
    global switch_list

    if switch_list[idx] == 0:
        switch_list[idx] = 1
    else:
        switch_list[idx] = 0


n = int(sys.stdin.readline().rstrip())
switch_list = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())

for _ in range(m):
    gender, cnt = map(int, sys.stdin.readline().rstrip().split())

    if gender == 1:
        for i in range(n):
            if (i + 1) % cnt == 0:
                change_swtich(i)
    if gender == 2:
        change_swtich(cnt - 1)

        i = 1
        while cnt - 1 + i < n and cnt - 1 - i >= 0:
            if switch_list[cnt - 1 + i] == switch_list[cnt - 1 - i]:
                change_swtich(cnt - 1 + i)
                change_swtich(cnt - 1 - i)
            else:
                break
            i += 1

for i in range(n // 20):
    print(*switch_list[20 * i:20 * (i + 1)])

if n % 20 != 0:
    print(*switch_list[20 * (n // 20):])
