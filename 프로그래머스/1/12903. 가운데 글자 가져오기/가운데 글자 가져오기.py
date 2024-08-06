def solution(s):
    length = len(s)
    if length % 2 == 1:
        
        answer = s[length // 2]
    else:
        mid = length // 2
        answer = s[mid - 1:mid + 1]
    return answer
