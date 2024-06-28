def solution(babbling):
    answer = 0
    valid_strings = ['aya', 'ye', 'woo', 'ma']
    
    for word in babbling:
        temp_word = word
        for valid in valid_strings:
            temp_word = temp_word.replace(valid, ' ')
        temp_word = temp_word.strip()
        
        if temp_word == '':
            answer += 1
    
    return answer

babbling = ['aya', 'yee', 'u', 'maa', 'wyeoo']
print(solution(babbling))

    
    
    
    