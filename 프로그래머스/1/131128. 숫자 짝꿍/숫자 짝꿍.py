def solution(X, Y):
    # 각 숫자의 빈도를 저장할 리스트
    count_X = [0] * 10
    count_Y = [0] * 10
    
    # X에서 각 숫자의 빈도 계산
    for digit in X:
        count_X[int(digit)] += 1
    
    # Y에서 각 숫자의 빈도 계산
    for digit in Y:
        count_Y[int(digit)] += 1
    
    # 공통으로 나타나는 숫자를 내림차순으로 모으기
    result = []
    
    for i in range(9, -1, -1):
        # 공통으로 나타나는 숫자의 최소 빈도만큼 추가
        common_count = min(count_X[i], count_Y[i])
        result.extend([str(i)] * common_count)
    
    # 결과가 비어있다면 짝꿍이 없음
    if not result:
        return "-1"
    
    # 결과가 모두 0이면 0 반환
    if result[0] == '0':
        return "0"
    
    # 리스트를 문자열로 변환 후 반환
    return "".join(result)
