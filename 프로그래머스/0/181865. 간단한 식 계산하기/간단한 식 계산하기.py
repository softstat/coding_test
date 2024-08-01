def solution(binomial):
    cal = binomial.split()
    a = int(cal[0])
    op = cal[1]
    b = int(cal[2])
    if op == "*":
        answer = a * b
    elif op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    
    return answer