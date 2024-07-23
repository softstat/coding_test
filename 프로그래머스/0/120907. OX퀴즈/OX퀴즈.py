def solution(quiz):
    answer = []
    for q in quiz:
        L,R = q.split("=")
        a,ot,b = L.split()
        if ot == "+":
            result =  "O" if int(a)+int(b) == int(R) else "X"
            answer.append(result)
        else:
            result= "O" if int(a)-int(b) == int(R) else "X"
            answer.append(result)
    return answer