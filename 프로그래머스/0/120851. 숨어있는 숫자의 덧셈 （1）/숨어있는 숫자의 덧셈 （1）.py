def solution(my_string):
    answer = 0
    data = []
    for i in my_string:
        if i.isnumeric()==True:
            data.append(int(i))
    answer = sum(data)
    return answer