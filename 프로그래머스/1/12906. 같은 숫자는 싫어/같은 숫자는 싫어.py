def solution(arr):
    answer = []
    a = None  

    for i in arr:
        if i != a:   
            answer.append(i)
            a = i       

    return answer
