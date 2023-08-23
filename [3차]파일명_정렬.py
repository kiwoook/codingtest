import re

def solution(files):
    answer = []

    for file in files:
        match = re.match(r'([a-zA-Z\-\n\s.]+)([0-9]{0,5})(.*)', file)
        print(match)
        if match:
            answer.append([match.group(1), int(match.group(2)), file])

    answer.sort(key=lambda x: (str(x[0]).lower(), x[1], files))
    return [a[2] for a in answer]


print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
