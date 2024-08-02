def solution(arr, n):
    answer = []
    if len(arr)%2==1:
        for key,value in enumerate(arr):
            if key%2==0:
                arr[key] += n
    if len(arr)%2==0:
        for key,value in enumerate(arr):
            if key%2==1:
                arr[key] += n
    return arr