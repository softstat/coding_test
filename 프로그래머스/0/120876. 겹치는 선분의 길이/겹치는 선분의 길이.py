def solution(lines):
    answer = 0
    s1 = set(i for i in range(lines[0][0],lines[0][1]))
    s2 = set(i for i in range(lines[1][0],lines[1][1]))
    s3 = set(i for i in range(lines[2][0],lines[2][1]))
    answer = len((s1&s2)|(s2&s3)|(s1&s3))
    return answer