def solution(n):
    # Calculate factorials until we find one greater than n
    factorial = 1
    i = 1
    while factorial <= n:
        i += 1
        factorial *= i
    
    # Return the largest factorial less than or equal to n
    return i - 1