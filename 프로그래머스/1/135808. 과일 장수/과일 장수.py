def solution(k, m, score):
    # 점수를 내림차순으로 정렬
    score.sort(reverse=True)
    
    # 최대 이익을 저장할 변수
    answer = 0
    
    # m개씩 묶어서 상자 만들기
    for i in range(0, len(score) - (len(score) % m), m):
        # 묶은 그룹에서 가장 작은 값이 상자의 가격을 결정
        box_price = min(score[i:i+m]) * m
        answer += box_price
    
    return answer

