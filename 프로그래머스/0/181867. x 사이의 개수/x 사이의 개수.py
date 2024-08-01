def solution(myString):
    answer = []
    parts = myString.split("x")
    print(parts)
    length = [len(part) for part in parts]
    return length