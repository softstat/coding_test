def solution(age):
    answer = ''
    age_str = str(age)
    
    for i in range(len(age_str)):
        if age_str[i] == "0":
            answer += "a"
        elif age_str[i] == "1":
            answer += "b"
        elif age_str[i] == "2":
            answer += "c"
        elif age_str[i] == "3":
            answer += "d"
        elif age_str[i] == "4":
            answer += "e"
        elif age_str[i] == "5":
            answer += "f"
        elif age_str[i] == "6":
            answer += "g"
        elif age_str[i] == "7":
            answer += "h"
        elif age_str[i] == "8":
            answer += "i"
        elif age_str[i] == "9":
            answer += "j"
        
    
    return answer