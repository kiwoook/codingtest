# from collections import deque
#
# like_list = ["4", "7"]
#
# k = int(input())
#
# q = deque([["4"], ["7"]])
#
# cnt = 1
# while q:
#     value = q.popleft()
#     if cnt == k:
#         print(*value)
#         break
#     cnt += 1
#     for i in range(2):
#         value.append(like_list[i])
#         q.append([''.join(value)])
# 범위가 존나 커서 메모리 초과가 나네요~~
# 이진수로 접근합시다....

k = int(input())
value = str(bin(k + 1)[3:])
print(value.replace('0', '4').replace('1', '7'))
