def solution(n):
    answer = []
    while n != 1:
        answer.append(n)
        if n % 2 == 0:
            n //= 2  # Use integer division to avoid float results
        else:
            n = 3 * n + 1
    answer.append(1)  # Append the final 1
    return answer
