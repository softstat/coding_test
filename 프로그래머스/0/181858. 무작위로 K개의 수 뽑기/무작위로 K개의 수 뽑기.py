def solution(arr, k):
    seen = set()       # To track unique numbers
    result = []        # To store the final list of unique numbers
    
    # Process each number in the array
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
        # If we have collected k unique numbers, stop processing
        if len(result) == k:
            break
    
    # If result length is less than k, pad with -1
    while len(result) < k:
        result.append(-1)
    
    return result
