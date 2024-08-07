def solution(arr1, arr2):
    answer = []
    for row1, row2 in zip(arr1, arr2):
        new_row = [x + y for x, y in zip(row1, row2)]
        answer.append(new_row)
    return answer