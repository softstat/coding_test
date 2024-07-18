def solution(n, k):
    answer = 12000*n + k*2000 - 2000*(n//10)
    return answer