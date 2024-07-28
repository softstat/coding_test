def solution(my_string, is_suffix):
    string = [my_string[i:] for i in range(len(my_string))]
    if is_suffix in string:
        return 1
    else:
        return 0