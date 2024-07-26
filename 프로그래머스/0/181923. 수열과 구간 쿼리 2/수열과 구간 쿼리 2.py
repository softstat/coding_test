def solution(arr, queries):
    answer = []
    for query in queries:
        start, end, threshold = query
        candidates = [x for x in arr[start:end+1] if x > threshold]
        if candidates:
            answer.append(min(candidates))
        else:
            answer.append(-1)
    return answer

