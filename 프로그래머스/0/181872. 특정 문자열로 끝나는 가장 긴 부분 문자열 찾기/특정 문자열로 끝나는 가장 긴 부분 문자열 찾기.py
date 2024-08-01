def solution(myString, pat):
    last_occurrence = myString.rfind(pat)

    if last_occurrence == -1:
        return ''
    return myString[:last_occurrence + len(pat)]