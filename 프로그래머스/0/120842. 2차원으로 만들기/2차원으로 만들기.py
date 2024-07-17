import numpy as np
def solution(num_list, n):
    answer = [[]]
    # Create the 2D list
    answer = [num_list[i:i + n] for i in range(0, len(num_list), n)]
    return answer