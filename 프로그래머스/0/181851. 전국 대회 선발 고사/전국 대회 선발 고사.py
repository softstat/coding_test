def solution(rank, attendance):
    # 실제 참석한 학생들의 인덱스를 담을 리스트
    real = []

    # 참석 여부가 True인 학생들의 인덱스를 real 리스트에 추가
    for idx, is_present in enumerate(attendance):
        if is_present:  # 참석 여부가 True이면
            real.append(idx)
    
    # 참석한 학생들의 순위를 기준으로 정렬
    real_sorted_by_rank = sorted(real, key=lambda x: rank[x])
    
    # 순위가 높은 세 학생의 인덱스 가져오기
    top_three = real_sorted_by_rank[:3]
    
    # 결과 계산
    answer = 10000 * top_three[0] + 100 * top_three[1] + top_three[2]
    
    return answer
