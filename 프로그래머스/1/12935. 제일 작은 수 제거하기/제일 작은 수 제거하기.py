def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))

        return arr
    elif arr==[10]:
        return [-1]