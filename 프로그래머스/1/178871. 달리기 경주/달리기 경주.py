def solution(players, callings):
    # 각 플레이어의 현재 순위를 저장하는 딕셔너리 생성
    rank_dic = {player: i for i, player in enumerate(players)}
    
    for player in callings:
        # 호출된 플레이어의 현재 순위를 가져옴
        current_rank = rank_dic[player]
        
        # 만약 현재 순위가 0보다 크면 (즉, 맨 앞이 아니면), 앞의 플레이어와 순서를 교환
        if current_rank > 0:
            # 앞에 있는 플레이어 찾기
            player_ahead = players[current_rank - 1]
            
            # 순서 교환
            players[current_rank - 1], players[current_rank] = players[current_rank], players[current_rank - 1]
            
            # 딕셔너리에서 각 플레이어의 순위 업데이트
            rank_dic[player] -= 1
            rank_dic[player_ahead] += 1

    return players
