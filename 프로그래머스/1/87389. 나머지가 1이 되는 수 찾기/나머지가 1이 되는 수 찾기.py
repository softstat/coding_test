def solution(n):
    answer = 0
    li = []
    for i in range(1,n):
        if n%i == 1:
            li.append(i)
    answer = min(li)
    return answer