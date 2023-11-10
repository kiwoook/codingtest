def solution(elements):
    elements_len = len(elements)
    elements = elements + elements
    set_hap = set()
    for i in range(1, elements_len + 1):
        for k in range(elements_len):
            set_hap.add(sum(elements[k:k + i]))

    return len(set_hap)

print(solution([7, 9, 1, 1, 4]))
