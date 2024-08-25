def solution(babbling):
    answer = 0
    valid = ['aya', 'ye', 'woo', 'ma']
    
    for word in babbling:
        for v in valid:
            if v*2 not in word:  # 동일한 발음이 연속되는지 확인
                word = word.replace(v, ' ')
        
        # 발음할 수 있는 단어라면 공백으로만 구성된 문자열이어야 함
        if word.strip() == '':
            answer += 1
    
    return answer

