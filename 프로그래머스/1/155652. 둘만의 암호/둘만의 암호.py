def solution(s, skip, index):
    answer = ''
    string = sorted(set("abcdefghijklmnopqrstuvwxyz") - set(skip))
    str_num = len(string)
    for char in s:
        answer += string[(string.index(char)+index)%str_num]
    return answer