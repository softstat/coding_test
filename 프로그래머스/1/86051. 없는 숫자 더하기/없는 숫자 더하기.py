def solution(numbers):
    answer = -1
    ten = [0,1,2,3,4,5,6,7,8,9]
    if numbers not in ten:
        answer = 45-sum(numbers)
    return answer