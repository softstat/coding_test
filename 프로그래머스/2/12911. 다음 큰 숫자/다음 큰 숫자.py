def solution(n):
    answer = 0
    double = bin(n)[2:]
    print(bin(n))
    for number in range(n+1, 1000000):
        next_double = bin(number)[2:]
        if next_double.count("1") == double.count("1"):
            answer = number
            break
        else:
            pass
    return answer