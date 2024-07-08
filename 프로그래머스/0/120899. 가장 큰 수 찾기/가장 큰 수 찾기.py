def solution(array):
    answer = []
    value = sorted(array)
    answer = [value[-1],array.index(value[-1])]
    return answer