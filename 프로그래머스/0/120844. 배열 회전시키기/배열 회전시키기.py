def solution(numbers, direction):
    answer = numbers*2
    if direction == "right":
        answer = answer[len(numbers)-1:len(numbers)+len(numbers)-1]
    if direction == "left":
        answer = answer[1:len(numbers)+1]
    return answer