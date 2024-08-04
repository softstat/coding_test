def solution(order):
    answer = 0
    element = {'americano': 4500, 'cafelatte': 5000}
    
    for i in order:
        if "americano" in i:
            answer += element['americano']
        elif "cafelatte" in i:
            answer += element['cafelatte']
        elif "anything" in i:
            answer += element['americano']  
    
    return answer