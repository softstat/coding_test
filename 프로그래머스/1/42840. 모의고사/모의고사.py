def solution(answers):
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cor1, cor2, cor3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == num1[i % len(num1)]: 
            cor1 += 1
        if answers[i] == num2[i % len(num2)]:
            cor2 += 1
        if answers[i] == num3[i % len(num3)]:
            cor3 += 1
    max_score = max(cor1, cor2, cor3)
    answer = []
    if cor1 == max_score:
        answer.append(1)
    if cor2 == max_score:
        answer.append(2)
    if cor3 == max_score:
        answer.append(3)
    
    return answer
