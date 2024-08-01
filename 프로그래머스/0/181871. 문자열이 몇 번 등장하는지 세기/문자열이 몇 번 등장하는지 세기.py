def solution(myString, pat):
    count = 0
    pat_len = len(pat)
    for i in range(len(myString) - pat_len + 1):
        if myString[i:i + pat_len] == pat:
            count += 1
            
    return count