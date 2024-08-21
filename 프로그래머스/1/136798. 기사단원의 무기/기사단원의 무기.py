def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        divisor_count = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                divisor_count += 1
                if j != i // j:
                    divisor_count += 1
        if divisor_count > limit:
            divisor_count = power
        answer += divisor_count
    
    return answer
