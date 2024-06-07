import sys

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
sensor_list = list(map(int, sys.stdin.readline().rstrip().split()))
diff_list = []

if k >= n:
    print(0)
else:
    sensor_list.sort()
    for i in range(len(sensor_list) - 1):
        diff_list.append(abs(sensor_list[i+1] - sensor_list[i]))

    diff_list.sort(reverse=True)

    hap = sum(diff_list[k-1:])

    print(hap)
