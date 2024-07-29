def solution(arr):
    answer = []
    l = [a for a,b in enumerate(arr) if b == 2]
    if len(l)==0:
        answer = [-1]
    else:
        answer = arr[min(l):max(l)+1]
    return answer