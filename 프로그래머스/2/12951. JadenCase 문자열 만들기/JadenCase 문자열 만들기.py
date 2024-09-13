def solution(s):

    S = s.lower()
    H = S.split(' ')
    STRING = []

    for i in H:
        print(i)
        if i:
            Z = i[0].upper() + i[1:]
        else:
            Z = i
        STRING.append(Z)
    last = ' '.join(STRING)

    return last