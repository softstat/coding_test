def solution(s):
    answer = 0
    dic = {"x": 0, "other": 0}
    x = ''
    
    for char in s:
        if dic["x"] == 0 and dic["other"] == 0: 
            x = char  
            dic["x"] = 1
        else:
            if char == x:
                dic["x"] += 1
            else:
                dic["other"] += 1

        if dic["x"] == dic["other"]:
            answer += 1  
            dic["x"] = 0 
            dic["other"] = 0
    if dic["x"] > 0 or dic["other"] > 0:
        answer += 1
    
    return answer
