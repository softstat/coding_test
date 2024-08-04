def solution(board, k):
    answer = 0
    rows = len(board)       
    cols = len(board[0])    
    
    for i in range(rows):
        for j in range(cols):
            if i + j <= k:
                answer += board[i][j] 
    
    return answer