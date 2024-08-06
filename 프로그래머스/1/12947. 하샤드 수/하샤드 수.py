def solution(x):
    answer = True
    fa = 0
    for i in str(x):
        fa += int(i)
        if x%fa==0:
            answer = True
        else:
            answer = False
    return answer