import sys

n, m = map(int, input().split())

password_dict = dict()

for _ in range(n):
    url, pw = sys.stdin.readline().rstrip().split()
    password_dict[url] = pw

for _ in range(m):
    url = sys.stdin.readline().rstrip()
    print(password_dict[url])