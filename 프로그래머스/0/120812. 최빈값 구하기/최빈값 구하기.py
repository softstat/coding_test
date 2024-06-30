def solution(array):
    answer = 0
    count = {}
    for i in array:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
     # Find the element with the highest count
    max_count = 0
    most_frequent = None
    tie = False
    
    for num, count in count.items():
        if count > max_count:
            max_count = count
            most_frequent = num
            tie = False
        elif count == max_count:
            tie = True
    
    # If there's a tie for the most frequent element, return -1
    if tie:
        return -1
    
    # Return the most frequent element
    return most_frequent
    return answer