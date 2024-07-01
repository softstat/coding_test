def solution(A, B):
    if A == B:
        return 0
    
    
    for i in range(1, len(A)):
        
        rotated_A = A[-i:] + A[:-i]
        if rotated_A == B:
            return i
    
    return -1