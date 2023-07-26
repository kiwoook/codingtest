def solution(brown, yellow):
    answer = []
    # (x-2) * (y-2) = yellow
    sw = 0
    for i in range(3, yellow+2+1):
        for x in range(3, i+1):
            for y in range(3, x+1):
                print(x,y)
                if (x-2)*(y-2) == yellow:
                    answer = [x, y]
                    sw =1
                    break
            if sw:
                break
        if sw:
            break
    return answer


solution(10,2)