from collections import deque, defaultdict

l = [-1] * 20
r = [-1] * 20
val = []
n = 0
ans = 1
visited =[]

def solution(info, edges):
    global n, val, visited


    sheep = 0
    n = len(info)
    val = info.copy()

    for u, v in edges:
        pass


    return sheep


# print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
#                [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))

print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
               [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
