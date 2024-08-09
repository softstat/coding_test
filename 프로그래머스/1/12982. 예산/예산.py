def solution(d, budget):
    d.sort()
    answer = 0
    total = 0
    
    for i in d:
        if total + i > budget:  
            break
        total += i 
        answer += 1
    
    return answer
