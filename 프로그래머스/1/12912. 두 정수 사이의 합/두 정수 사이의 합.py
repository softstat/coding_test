def solution(a, b):
    answer = 0
    answer = sum(x for x in range(a,b+1)) or sum(x for x in range(b,a+1))
    return answer