def solution(my_string, indices):
    answer = list(my_string)
    for i in sorted(indices, reverse=True):
        answer.pop(i)
    return ''.join(answer)
