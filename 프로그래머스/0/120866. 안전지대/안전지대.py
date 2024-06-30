def solution(board):
    answer = 0
    rows = len(board)
    cols = len(board[0])
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:  # 현재 위치에 지뢰가 있는 경우
                # 현재 위치와 그 주변 8방향을 모두 위험 지역으로 처리합니다.
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < rows and 0 <= nj < cols:
                            if board[ni][nj] == 0:  # 지뢰도 없고 위험 지역도 아닌 경우
                                board[ni][nj] = -1  # -1은 위험 지역을 나타냅니다.
    
    # 안전 지역의 개수를 세기 위해 board를 다시 순회합니다.
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 0:  # 지뢰도 없고 위험 지역도 아닌 경우
                answer += 1  # 안전한 지역으로 카운트합니다.
    
    return answer




