def solution(date1, date2):
    str1 = ''
    for num in date1:
        str1 += str(num)
    str2 = ''
    for num in date2:
        str2 += str(num)
    if int(str1) >= int(str2):
        return 0
    else:
        return 1
