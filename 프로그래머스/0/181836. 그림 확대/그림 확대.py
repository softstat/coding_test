def solution(picture, k):
    answer = []
    for ele in picture:
        char = ''.join(chr*k for chr in ele)
        for _ in range(k):
            answer.append(char)
    return answer
