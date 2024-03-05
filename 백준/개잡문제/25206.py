import sys

cnt = 0
total_score = 0
grade_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
for _ in range(20):
    subject, score, grade = sys.stdin.readline().rstrip().split()
    score = float(score)

    if grade == 'P':
        continue
    else:
        total_score += score
        cnt += score * grade_dict[grade]

print("{:.5f}".format(cnt / total_score))
