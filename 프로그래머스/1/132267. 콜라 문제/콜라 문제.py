def solution(a, b, n):
    answer = 0
    
    while n >= a:
        d = n // a
        c = n % a   
        n = d * b + c  
        answer += d * b  
    
    return answer