def solution(num_list):
    p = 0 
    q = 0  
    for i in num_list:
        if i % 2 == 0:
            p += 1
        else:
            q += 1
    answer = [p, q]
    return answer
