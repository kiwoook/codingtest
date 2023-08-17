from collections import Counter


def solution(str1, str2):
    list1 = []
    list2 = []
    str1_list = []
    str2_list = []

    for i in range(len(str1) - 1):
        list1.append(str1[i:i + 2])
    for i in range(len(str2) - 1):
        list2.append(str2[i:i + 2])

    for idx, s1 in enumerate(list1):
        s1 = str(s1)
        if s1.isalpha():
            str1_list.append(s1.lower())
    for idx, s2 in enumerate(list2):
        s2 = str(s2)
        if s2.isalpha():
            str2_list.append(s2.lower())

    str1_list.sort()
    str2_list.sort()
    if str1_list == str2_list:
        return 65536

    counter1 = Counter(str1_list)
    counter2 = Counter(str2_list)

    intersection = len(list((counter1 & counter2).elements()))  # 교집합
    union = len(list((counter1 | counter2).elements()))  # 합집합

    return int(intersection / union * 65536)


print(solution("aa1+aa2", "AAAA12"))
print(solution("AAbbaa_AAbb", "BBB"))
