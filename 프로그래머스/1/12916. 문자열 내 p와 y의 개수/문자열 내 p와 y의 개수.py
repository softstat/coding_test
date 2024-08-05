def solution(s):
    answer = True
    count1 = 0
    count2 = 0
    s = s.lower()
    count1 = s.count('p')
    count2 = s.count('y')
    if count1 == count2:
        return True
    else:
        return False