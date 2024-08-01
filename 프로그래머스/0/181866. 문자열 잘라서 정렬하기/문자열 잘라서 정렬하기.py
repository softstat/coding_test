def solution(myString):
    parts = myString.split('x')
    answer = sorted(part for part in parts if part)
    return answer