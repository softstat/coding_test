def solution(myString, pat):
    myString = myString.replace("A","1")
    myString = myString.replace("B","2")
    myString = myString.replace("1","B")
    myString = myString.replace("2","A")
    if pat in myString:
        return 1
    else:
        return 0