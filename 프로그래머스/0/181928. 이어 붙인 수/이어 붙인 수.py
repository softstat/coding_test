def solution(num_list):
    str1 = ''
    str2 = ''
    for i in num_list:
        if i % 2 == 0:
            str1 += str(i)  
        else:
            str2 += str(i)  

    answer = int(str1) + int(str2)
    return answer
