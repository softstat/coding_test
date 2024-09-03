def solution(ingredient):
    answer = 0    
    i = 0
    while i != len(ingredient):
        if ingredient[i:i+4] == [1, 2, 3, 1]:
            answer += 1
            del ingredient[i:i+4]
            if i - 4 > 0:
                i = i - 4
            else:
                i = 0
        else:
            i += 1
    
    return answer

