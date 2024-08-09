def solution(array, commands):
    answer = []
    for q in commands:
        a,b,c = q
        v1 = sorted(array[a-1:b])[c-1]
        answer.append(v1)
    return answer