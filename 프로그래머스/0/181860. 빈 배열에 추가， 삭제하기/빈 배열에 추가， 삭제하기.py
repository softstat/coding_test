def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i]:
            for _ in range(arr[i] * 2):
                answer.append(arr[i])
        else:
            for _ in range(arr[i]):
                if answer:
                    answer.pop()
    return answer
