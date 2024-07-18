def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = numbers[i] * numbers[j]
            if product > answer:
                answer = product
    
    return answer