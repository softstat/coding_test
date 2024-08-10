def solution(s, n):
    answer = ''
    lower_list = 'abcdefghijklmnopqrstuvwxyz'
    upper_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in s:
        if i.isupper():
            idx = upper_list.index(i)
            answer += upper_list[(idx + n) % 26]
        elif i.islower():
            idx = lower_list.index(i)
            answer += lower_list[(idx + n) % 26]
        else:
            answer += i
    
    return answer
