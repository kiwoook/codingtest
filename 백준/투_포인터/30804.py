from collections import defaultdict


# 우선 총 과일의 수를 스캔해야함
# 앞 뒤 뺴는 건 우선 신경쓰지말자

def available_tanghuru():
    cnt = 0
    for key, value in fruit_dict.items():
        if value > 0:
            cnt += 1

    if cnt <= 2:
        return True

    return False


answer = 0

n = int(input())
s = list(map(int, input().split()))
fruit_dict = defaultdict(int)

# 과일 번호는 9개밖에안됨

left, right = 0, 0
fruit_dict[right] += 1

while left <= right < n:
    print(left, right, fruit_dict)
    if available_tanghuru():
        answer = max(answer, right - left)
        right += 1
        if right < n:
            fruit_dict[right] += 1
    else:
        fruit_dict[left] -= 1
        left += 1

print(answer)
