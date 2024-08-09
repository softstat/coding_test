def solution(n):
    string = ''
    while n > 0:
        n, remainder = divmod(n, 3)
        string = str(remainder) + string  

    reversed_string = string[::-1]
    answer = int(reversed_string, 3)
    
    return answer

