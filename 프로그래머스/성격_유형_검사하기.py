def solution(survey, choices):
    answer = ''
    indicator = [{'R': 0, 'T': 0}, {'C': 0, 'F': 0}, {'J': 0, 'M': 0}, {'A': 0, 'N': 0}]
    survey_len = len(survey)
    survey_dict = {"RT": 0, "TR": 0, "FC": 1, "CF": 1, "MJ": 2, "JM": 2, "AN": 3, "NA": 3}
    for i in range(survey_len):
        if choices[i] > 4:
            indicator[survey_dict[survey[i]]][survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            indicator[survey_dict[survey[i]]][survey[i][0]] -= choices[i] - 4

    for i in indicator:
        max_value = max(i.values())
        for key, value in i.items():
            if value == max_value:
                answer += key
                break
    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
