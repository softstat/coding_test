def solution(my_string):
    answer = 0
    current_number = ''
    
    for char in my_string:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                answer += int(current_number)
                current_number = ''
    
    if current_number:  # To add any number left at the end of the string
        answer += int(current_number)
    
    return answer

