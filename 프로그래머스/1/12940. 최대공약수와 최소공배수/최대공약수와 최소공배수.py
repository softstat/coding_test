def solution(n, m):
    answer = []
    num1 = 0
    for i in range(1,n+1):
        if n%i==0 and m%i==0:
            num1 = i
    num2 = int(n*m/num1)
    answer = [num1,num2]
    return answer