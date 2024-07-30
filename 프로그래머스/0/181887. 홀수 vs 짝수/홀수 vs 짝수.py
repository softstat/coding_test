def solution(num_list):
    a = 0
    b = 0
    for idx, value in enumerate(num_list):
        if idx % 2 == 0:
            a += value
        else:
            b += value
    return max(a, b)