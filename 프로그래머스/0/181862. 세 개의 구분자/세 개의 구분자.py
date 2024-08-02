def solution(myStr):
    myStr = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ')
    answer = myStr.split(' ')
    answer = [s for s in answer if len(s)>0]
    if not answer:
        return ["EMPTY"]
    
    return answer