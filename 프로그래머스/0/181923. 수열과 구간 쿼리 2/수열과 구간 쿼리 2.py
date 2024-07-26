def solution(arr, queries):
    answer = []
    for a,b,c in queries:
        sol = [x for x in arr[a:b+1] if x>c]
        
        if sol:
            answer.append(min(sol))
        else:
            answer.append(-1)
    return answer