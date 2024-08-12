def solution(food):
    first = []
    for i in range(1, len(food)):
        first.extend([str(i)] * (food[i] // 2))
    answer = ''.join(first) + '0' + ''.join(first[::-1])
    
    return answer
