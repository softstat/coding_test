def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    zero = 0
    cor = 0
    for i in lottos:
        if i == 0:
            zero += 1
        elif i in win_nums:
            cor += 1
    max_rank = rank[cor + zero]
    min_rank = rank[cor]
    
    return [max_rank, min_rank]
