def solution(arr1, arr2):
    answer = 0
    if len(arr2)>len(arr1):
        return -1
    if len(arr2) == len(arr1):
        if sum(arr2)>sum(arr1):
            return -1
        elif sum(arr2)<sum(arr1):
            return 1
        elif sum(arr1) == sum(arr2):
            return 0
    if len(arr1)>len(arr2):
        return 1
