def solution(n):
    answer = ''
    a = n // 2
    b = n % 2
    answer = a * "수박" + b * "수"
    return answer
