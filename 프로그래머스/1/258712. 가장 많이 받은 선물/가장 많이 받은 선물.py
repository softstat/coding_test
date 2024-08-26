def solution(friends, gifts):
    # 1. 각 친구가 준 선물과 받은 선물을 기록할 딕셔너리 생성
    give_count = {friend: 0 for friend in friends}
    receive_count = {friend: 0 for friend in friends}
    
    # 2. 선물 기록을 기반으로 준 사람과 받은 사람 기록
    for gift in gifts:
        giver, receiver = gift.split()
        give_count[giver] += 1
        receive_count[receiver] += 1
    
    # 3. 선물 지수 계산 (준 선물 수 - 받은 선물 수)
    gift_index = {friend: give_count[friend] - receive_count[friend] for friend in friends}
    
    # 4. 다음 달에 받을 선물 수 계산
    next_month_gifts = {friend: 0 for friend in friends}
    
    # 친구 쌍마다 비교를 위해 모든 친구 쌍을 확인
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            f1, f2 = friends[i], friends[j]
            f1_to_f2 = gifts.count(f"{f1} {f2}")
            f2_to_f1 = gifts.count(f"{f2} {f1}")
            
            if f1_to_f2 > f2_to_f1:
                next_month_gifts[f1] += 1
            elif f2_to_f1 > f1_to_f2:
                next_month_gifts[f2] += 1
            else:
                # 주고받은 선물 수가 같은 경우, 선물 지수를 비교
                if gift_index[f1] > gift_index[f2]:
                    next_month_gifts[f1] += 1
                elif gift_index[f2] > gift_index[f1]:
                    next_month_gifts[f2] += 1
    
    # 5. 가장 많이 선물을 받을 친구가 받을 선물 수 반환
    max_gifts = max(next_month_gifts.values())
    
    return max_gifts
