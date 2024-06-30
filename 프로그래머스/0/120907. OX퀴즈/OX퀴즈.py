def solution(quiz):
    answer = []
    for q in quiz:
        # Split the quiz string into parts
        parts = q.split()
        
        # Extract the left-hand side (lhs) and right-hand side (rhs) of the equation
        lhs = parts[0] + ' ' + parts[1] + ' ' + parts[2]  # e.g., "3 - 4"
        rhs = parts[4]  # e.g., "-1"
        
        # Evaluate the lhs and compare it with rhs
        if eval(lhs) == int(rhs):
            answer.append("O")
        else:
            answer.append("X")
            
    return answer



