def solution(s):
    # 공백을 기준으로 문자열을 분리하여 숫자 리스트로 변환
    numbers = list(map(int, s.split()))
    
    # 최소값과 최대값을 찾기
    min_value = min(numbers)
    max_value = max(numbers)
    
    # "(최소값) (최대값)" 형태의 문자열을 반환
    return f"{min_value} {max_value}"

