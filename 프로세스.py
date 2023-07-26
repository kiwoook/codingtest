from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    while 1:
        max_value = max(priorities)
        chk_value = priorities.popleft()
        if location == 0:
            if chk_value >= max_value:
                answer += 1
                return answer
            else:
                priorities.append(chk_value)
                location = len(priorities)-1
        else:
            location -= 1
            if chk_value < max_value:
                priorities.append(chk_value)
            else:
                answer += 1



print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],  0))