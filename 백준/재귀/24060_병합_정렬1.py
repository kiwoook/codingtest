import sys

v = 0


def merge_sort(arr):
    def sort(low, high):

        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        return merge(low, mid, high)

    def merge(low, mid, high):
        global v
        tmp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                tmp.append(arr[l])
                l += 1
            else:
                tmp.append(arr[h])
                h += 1
        while l < mid:
            tmp.append(arr[l])
            l += 1
        while h < high:
            tmp.append(arr[h])
            h += 1

        for i in range(low, high):
            v += 1
            if v == k:
                print(arr[i])
            arr[i] = tmp[i - low]


        return tmp

    return sort(0, len(arr))


n, k = map(int, input().split())

a = list(map(int, sys.stdin.readline().rstrip().split()))
print(merge_sort(a))
