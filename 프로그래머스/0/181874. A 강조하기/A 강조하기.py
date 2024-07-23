def solution(myString):
    answer = ''
    for v in myString:
        if v == 'a':
            answer += v.upper()
        elif v == 'A':
            answer += v
        else:
            answer += v.lower()
    return answer

