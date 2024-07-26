def solution(numLog):
    answer = ''
    control = {1: "w", -1: "s", 10: "d", -10: "a"}
    
    # Iterate over numLog and calculate the differences
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i - 1]
        if diff in control:
            answer += control[diff]
    
    return answer
