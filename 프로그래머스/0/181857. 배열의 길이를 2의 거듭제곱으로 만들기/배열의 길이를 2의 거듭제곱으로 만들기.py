def solution(arr):
    length = len(arr)
    power_of_two = 1
    while power_of_two < length:
        power_of_two *= 2
    answer = arr + [0] * (power_of_two - length)
    
    return answer

