def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        combined = arr1[i] | arr2[i]
        binary_str = bin(combined)[2:].zfill(n)
        map_str = binary_str.replace('1', '#').replace('0', ' ')
        answer.append(map_str)
    
    return answer
