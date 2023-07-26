from itertools import combinations

def solution(clothes):
    answer = 1
    dict_clothes = {}

    for clothe, category in clothes:
        if category not in dict_clothes:
            dict_clothes[category] = []
        dict_clothes[category].append(clothe)

    for dict_cloth in dict_clothes.keys():
        answer *= len(dict_clothes[dict_cloth]) + 1

    return answer-1




print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))