def solution(polynomial):
    terms = polynomial.split(" + ")
    coefficient_sum = 0
    constant_sum = 0
    
    for term in terms:
        if 'x' in term:
            if term == 'x':
                coefficient_sum += 1
            else:
                coefficient_sum += int(term.replace('x', ''))
        else:
            constant_sum += int(term)
    
    answer = ''
    if coefficient_sum > 0:
        if coefficient_sum == 1:
            answer += 'x'
        else:
            answer += f'{coefficient_sum}x'
    if constant_sum > 0:
        if answer:
            answer += ' + '
        answer += str(constant_sum)
    
    return answer