def solution(k, score):
    li = []  
    answer = []

    for i in score:
        li.append(i)
        li.sort(reverse=True) 
        
        if len(li) > k:
            li.pop()
        
        answer.append(li[-1])

    return answer
