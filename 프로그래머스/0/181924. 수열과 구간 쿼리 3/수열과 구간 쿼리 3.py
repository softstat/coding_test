def solution(arr, queries):
    for p, q in queries:
        arr[p], arr[q] = arr[q], arr[p]
    return arr
