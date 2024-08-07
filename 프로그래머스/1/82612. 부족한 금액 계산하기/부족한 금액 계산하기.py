def solution(price, money, count):
    answer = -1
    pr = 0
    for i in range(count+1):
        pr += price*i
        answer = pr-money
    if money>pr:
        answer = 0
    return answer