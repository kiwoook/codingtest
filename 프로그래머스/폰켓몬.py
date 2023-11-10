def solution(nums):
    n = len(nums) / 2

    set_nums = set(nums)

    if n >= len(set_nums):
        return len(set_nums)
    else:
        return n


print(solution([3, 3, 3, 2, 2, 2]))
