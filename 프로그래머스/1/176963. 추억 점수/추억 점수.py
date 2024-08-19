def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning))
    for p in photo:
        total_yearning = 0
        for person in p:
            if person in dic:
                total_yearning += dic[person]  
        answer.append(total_yearning)
    
    return answer
