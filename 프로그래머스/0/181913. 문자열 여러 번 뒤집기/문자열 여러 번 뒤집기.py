def solution(my_string, queries):
    # Convert the string to a list of characters for mutability
    my_list = list(my_string)
    
    # Process each query
    for s, e in queries:
        # Reverse the sublist from index s to e using swaps
        while s < e:
            my_list[s], my_list[e] = my_list[e], my_list[s]
            s += 1
            e -= 1
    
    # Convert the list back to a string
    return ''.join(my_list)
