import sys


def is_pallindrome(v):
    left = 0
    right = len(v) - 1

    while left <= right:

        if v[left] == v[right]:
            left += 1
            right -= 1
        else:
            if left <= right - 1:
                tmp = v[:right] + v[right + 1:]
                if tmp[:] == tmp[::-1]:
                    return 1
            if left + 1 <= right:
                tmp = v[:left] + v[left + 1:]
                if tmp[:] == tmp[::-1]:
                    return 1
            return 2

    return 0


n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    # 회문 탐색
    word = sys.stdin.readline().rstrip()

    print(is_pallindrome(word))
