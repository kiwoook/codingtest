import sys

string = sys.stdin.readline().rstrip()

alpha_dict = dict()

for i in range(ord('a'), ord('z') + 1):
    char = chr(i)
    alpha_dict[char] = [0]
    cnt = 0
    for s in string:
        if s == char:
            cnt += 1
        alpha_dict[char].append(cnt)

q = int(sys.stdin.readline().rstrip())

for _ in range(q):
    char, start, end = sys.stdin.readline().rstrip().split()
    start = int(start)
    end = int(end)

    print(alpha_dict[char][end + 1] - alpha_dict[char][start])
