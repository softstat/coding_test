def solution(a, d, included):
    answer = 0
    for idx, value in enumerate(included):
        if value:
            answer += a + d * idx
    return answer
